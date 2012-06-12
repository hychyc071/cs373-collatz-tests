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

    def test_read_1_1_100 (self) :
        r = StringIO.StringIO("1 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 100)
        
    def test_read_2_100_1 (self) :
        r = StringIO.StringIO("100 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 1)
        
    def test_read_3_1_999999 (self) :
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 999999)
        
    def test_read_4_1_1 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)
        
    def test_read_5_2_2 (self) :
        r = StringIO.StringIO("2 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 2)
        self.assert_(a[1] == 2)
        
    def test_read_6_999999_999999 (self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 999999)
        self.assert_(a[1] == 999999)
        
    def test_read_7_100_800 (self) :
        r = StringIO.StringIO("100 800\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 800)

    # ----
    # eval
    # ----

    def test_eval_1_1_1 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_2_2_2 (self) :
        v = collatz_eval(2, 2)
        self.assert_(v == 2)

    def test_eval_3_999999_999999 (self) :
        v = collatz_eval(999999, 999999)
        self.assert_(v == 259)

    def test_eval_4_1_999999 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
        
    def test_eval_5_999999_1 (self) :
        v = collatz_eval(999999, 1)
        self.assert_(v == 525)
        
    def test_eval_6_1_999999 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
        
    def test_eval_7_10972_13254 (self) :
        v = collatz_eval(10792, 13254)
        self.assert_(v == 268)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assert_(w.getvalue() == "1 999999 525\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 999999\n999999 1\n1 1\n1 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n999999 1 525\n1 1 1\n1 2 2\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("3695 12341\n3695 3695\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3695 12341 268\n3695 3695 207\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_solve_5 (self) :
        r = StringIO.StringIO("1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n")
        
    def test_solve_6 (self) :
        r = StringIO.StringIO("999999 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999999 1 525\n")





# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."