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

from Collatz import catch, metacatch, collatz_read, collatz_eval, collatz_count, collatz_print, collatz_solve

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
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 999999)

    def test_read_3 (self) :
        r = StringIO.StringIO("999999 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 1)

    def test_read_4 (self) :
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 999999)

    def test_read_5 (self) :
        r = StringIO.StringIO("1111 1111\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1111)
        self.assert_(a[1] == 1111)

    def test_read_6 (self) :
        r = StringIO.StringIO("12 342\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  12)
        self.assert_(a[1] == 342)

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
        v = collatz_eval(589681, 87728)
        self.assert_(v == 470)

    def test_eval_7 (self) :
        v = collatz_eval(593993, 768068)
        self.assert_(v == 509)

    def test_eval_8 (self) :
        v = collatz_eval(5814, 453618)
        self.assert_(v == 449)

    def test_eval_9 (self) :
        v = collatz_eval(1999, 3000)
        self.assert_(v == 217)
	
    # -----
    # Count
    # -----

    def test_count_1 (self) :
        c = collatz_count(1)
        self.assert_(c == 1)
		
    def test_count_2 (self) :
        c = collatz_count(10)
        self.assert_(c == 7)	

    def test_count_3 (self) :
        c = collatz_count(100)
        self.assert_(c == 26)
		
    def test_count_4 (self) :
        c = collatz_count(123)
        self.assert_(c == 47)
		
    def test_count_5 (self) :
        c = collatz_count(999999)
        self.assert_(c == 259)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 123, 123, 123)
        self.assert_(w.getvalue() == "123 123 123\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 678, 124, 97)
        self.assert_(w.getvalue() == "678 124 97\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 12, 342, 6436)
        self.assert_(w.getvalue() == "12 342 6436\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 0, 0)
        self.assert_(w.getvalue() == "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 999999\n999999 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n999999 1 525\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1\n10 10\n100 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n10 10 7\n100 100 26\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("169530 563234\n72876 26368\n727821 671558\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "169530 563234 470\n72876 26368 340\n727821 671558 504\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("267834 348918\n314370 240312\n509355 125029\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "267834 348918 441\n314370 240312 407\n509355 125029 449\n")

    def test_solve_6 (self) :
        r = StringIO.StringIO("104693 814432\n409893 161478\n357275 499194\n278680 945701\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "104693 814432 509\n409893 161478 443\n357275 499194 449\n278680 945701 525\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
