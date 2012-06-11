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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc

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
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_space (self) :
        r = StringIO.StringIO("2        5\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(a[1] == 5)

    def test_read_tab (self) :
        r = StringIO.StringIO("8  \t 8\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  8)
        self.assert_(a[1] == 8)


    # ----
    # calc
    # ----

    def test_calc_1 (self) :
        v = collatz_calc(8)
        self.assert_(v == 4)

    def test_calc_2 (self) :
        v = collatz_calc(22)
        self.assert_(v == 16)

    def test_calc_3 (self) :
        v = collatz_calc(16)
        self.assert_(v == 5)

    def test_calc_4 (self) :
        v = collatz_calc(459759)
        self.assert_(v == 214)


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
        v = collatz_eval(482659, 474574)
        self.assert_(v == 413)

    def test_eval_6 (self) :
        v = collatz_eval(232545, 681701)
        self.assert_(v == 509)

    def test_eval_7 (self) :
        v = collatz_eval(773104, 675975)
        self.assert_(v == 504)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 8, 8, 5)
        self.assert_(w.getvalue() == "8 8 5\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 10\n201 210\n900 1000\n8 8\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n201 210 89\n900 1000 174\n8 8 4\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
