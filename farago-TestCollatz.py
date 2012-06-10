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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
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

    def test_read1 (self) :
        r = StringIO.StringIO("20 30\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 30)

    def test_read2 (self) :
        r = StringIO.StringIO("25 45\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 25)
        self.assert_(a[1] == 45)

    def test_read3 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)


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

    def test_eval_5 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)

    def test_eval_6 (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_7 (self) :
        v = collatz_eval(1000,2000)
        self.assert_(v == 182)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 15, 30)
        self.assert_(w.getvalue() == "2 15 30\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 30, 20)
        self.assert_(w.getvalue() == "10 30 20\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 100, 200)
        self.assert_(w.getvalue() == "100 100 200\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 1\n2 2\n1 3\n4 5\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n1 3 8\n4 5 6\n1 10 20\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 1000000\n155 156\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000000 525\n155 156 86\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
