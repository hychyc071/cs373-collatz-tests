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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("10000 54638\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10000)
        self.assert_(a[1] == 54638)

    def test_read_3 (self) :
        r = StringIO.StringIO("100000 100000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100000)
        self.assert_(a[1] == 100000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_3 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_4 (self) :
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_5 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_6 (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_7 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_8 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)
    
    
    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        n = 1
        i = 1
        j = 10
        cache = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        v = cycle_length(n, i, j, cache)
        expected_cache = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assert_(v == 1)
        self.assert_(cache == expected_cache)

    def test_cycle_length_2 (self) :
        n = 3
        i = 1
        j = 10
        cache = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        v = cycle_length(n, i, j, cache)
        expected_cache = [1, 2, 0, 3, 6, 0, 0, 4, 0, 0]
        self.assert_(v == 8)
        self.assert_(cache == expected_cache)

    def test_cycle_length_3 (self) :
        n = 5
        i = 1
        j = 10
        cache = [1, 2, 0, 3, 6, 0, 0, 4, 0, 0]
        v = cycle_length(n, i, j, cache)
        expected_cache = [1, 2, 0, 3, 6, 0, 0, 4, 0, 0]
        self.assert_(v == 6)
        self.assert_(cache == expected_cache)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 20, 1, 10)
        self.assert_(w.getvalue() == "20 1 10\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("647974 327422\n174014 474886\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "647974 327422 509\n174014 474886 449\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("44348 604259 470\n606229 217609 470\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "44348 604259 470\n606229 217609 470\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
