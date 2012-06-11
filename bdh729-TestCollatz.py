#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# Extra Unit Tests added by Benjamin Harris -- bdh729
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_do

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    
    # ----
    # do
    # ----
    
    def test_do (self) :
		v = collatz_do (1)
		self.assert_(v == 1)
		
    def test_do1 (self) :
		v = collatz_do (999999)
		self.assert_(v == 259)
		
    def test_do2 (self) :
		v = collatz_do (123456) 
		self.assert_(v == 62)
	
	#should assertion error fail	
    #def test_do3 (self) :
	#	v = collatz_do (0)
	#	self.assert_(v == 1) 
    
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
        
    def test_read1 (self) :
		r = StringIO.StringIO("1 1\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 1)
		self.assert_(a[1] == 1)
		
    def test_read2 (self) :
		r = StringIO.StringIO("999999 999999\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 999999)
		self.assert_(a[1] == 999999)

    def test_read2 (self) :
		r = StringIO.StringIO("1 999999\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 1)
		self.assert_(a[1] == 999999)
		
		
    #shouldn't fail
    def test_read2 (self) :
		r = StringIO.StringIO("")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == False)
		self.assert_(a[0] == 0)
		self.assert_(a[1] == 0)
    
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
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_6 (self) :
        v = collatz_eval(2, 2)
        self.assert_(v == 2)
        
    def test_eval_7 (self) :
        v = collatz_eval(999999, 999999)
        self.assert_(v == 259)
        
    def test_eval_8 (self) :
		v = collatz_eval(210, 201)
		self.assert_(v == 89)
		
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 999999, 259)
        self.assert_(w.getvalue() == "999999 999999 259\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999888, 999999, 259)
        self.assert_(w.getvalue() == "999888 999999 259\n")
        
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("1 1\n999999 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n999999 999999 259\n")
        
    def test_solve2 (self) :
        r = StringIO.StringIO("2 2\n3 3\n5 5\n10 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "2 2 2\n3 3 8\n5 5 6\n10 10 7\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("999999 999999\n999999 999999\n1 1\n2 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999999 999999 259\n999999 999999 259\n1 1 1\n2 2 2\n")
       
    def test_solve4 (self) :
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
