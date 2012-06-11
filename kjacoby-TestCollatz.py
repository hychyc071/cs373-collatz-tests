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
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

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
        v = collatz_eval(347, 669)
        self.assert_(v == 145)
    
    def test_eval_6 (self) :
        v = collatz_eval(98, 542)
        self.assert_(v == 144)
    
    def test_eval_7 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)


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
        collatz_print(w, 50, 163, 122)
        self.assert_(w.getvalue() == "50 163 122\n")
    
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 341, 342, 126)
        self.assert_(w.getvalue() == "341 342 126\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	
	def test_solve_2 (self) :
		r = StringIO.StringIO("1 20\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 20 21\n900 1000 174\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("390 806\n122 753\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "390 806 171\n122 753 171\n")
    
    def test_solve_4 (self) :
        r = StringIO.StringIO("82 935\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "82 935 179\n")
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
