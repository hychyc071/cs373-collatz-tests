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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_of

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
        r = StringIO.StringIO("500 500\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  500)
        self.assert_(a[1] == 500)
    
    def test_read_3 (self) :
        r = StringIO.StringIO("36 42\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  36)
        self.assert_(a[1] == 42)
    
    def test_read_4 (self) :
        r = StringIO.StringIO("700000 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  700000)
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
        v = collatz_eval(1, 29)
        self.assert_(v == 112)

    def test_eval_6 (self) :
        v = collatz_eval(40, 60)
        self.assert_(v == 113)

    def test_eval_7 (self) :
        v = collatz_eval(906167, 906167)
        self.assert_(v == 264)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 77)
        self.assert_(w.getvalue() == "10 1 77\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 88, 88, 88)
        self.assert_(w.getvalue() == "88 88 88\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 999, -35)
        self.assert_(w.getvalue() == "1000 999 -35\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
		
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n2 2\n3 3\n4 4\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n3 3 8\n4 4 3\n")
		
    def test_solve_3 (self) :
        r = StringIO.StringIO("16 16\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "16 16 5\n")
		
    def test_solve_4 (self) :
        r = StringIO.StringIO("64 64\n74 80\n100 110\n200 205\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "64 64 7\n74 80 36\n100 110 114\n200 205 40\n")
		
	# --------
    # cycle of
    # --------

    def test_cycle_of_1 (self) :
        i = cycle_of(1000)
        self.assert_(i == 112)
		
    def test_cycle_of_2 (self) :
        i = cycle_of(10000)
        self.assert_(i == 30)
		
    def test_cycle_of_3 (self) :
        i = cycle_of(100000)
        self.assert_(i == 129)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
