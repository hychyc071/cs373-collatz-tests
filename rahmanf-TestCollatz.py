#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
% python TestCollatz.py > TestCollatz.py.out
% chmod ugo+x TestCollatz.py
% TestCollatz.py > TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_cycle, collatz_solve, cache_setup

# -----------
# TestCollatz
# -----------
class TestCollatz (unittest.TestCase) :
    # -----------
    # cache setup
    # -----------
    
    def test_cache_setup (self) :
        cycle = cache_setup()
        self.assert_(cycle[2] == 2)

    def test_cache_setup_2 (self) :
        cycle = cache_setup()
        self.assert_(cycle[128] == 8)

    def test_cache_setup_3 (self) :
        cycle = cache_setup()
        self.assert_(cycle[524288] == 20)

    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)

    def test_read_3 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 201)
        self.assert_(a[1] == 210)

    def test_read_4 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 900)
        self.assert_(a[1] == 1000)

    # -----
    # cycle
    # -----

    def test_cycle (self) :
        c = collatz_cycle(5)
        self.assert_(c == 6)

    def test_cycle_2 (self) :
        c = collatz_cycle(16)
        self.assert_(c == 5)

    def test_cycle_3 (self) :
        c = collatz_cycle(127)
        self.assert_(c == 47)
 

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
