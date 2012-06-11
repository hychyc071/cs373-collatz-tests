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

from Collatz import collatz_read, collatz_eval, collatz_eval_help, collatz_print, collatz_solve

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
		
    def test_read_2 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)
	
    def test_read_4 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 900)
        self.assert_(a[1] == 1000)
		
		
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
	dic = {}
        v = collatz_eval(1, 10, dic)
        self.assert_(v == 20)

    def test_eval_2 (self) :
	dic = {}
        v = collatz_eval(100, 200, dic)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        dic = {}
	v = collatz_eval(201, 210, dic)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        dic = {}
	v = collatz_eval(900, 1000, dic)
        self.assert_(v == 174)

	# ----
    # eval_help
    # ----

    def test_eval_help_1 (self) :
	dic = {}
        v = collatz_eval_help(1, dic)
        self.assert_(v == 1)

    def test_eval_help_2 (self) :
	dic = {}
        v = collatz_eval_help(200, dic)
        self.assert_(v == 27)

    def test_eval_help_3 (self) :
	dic = {}
        v = collatz_eval_help(1000000, dic)
        self.assert_(v == 153)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	
    def test_solve_2(self) :
        r = StringIO.StringIO("100 200\n201 210\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 200 125\n201 210 89\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
