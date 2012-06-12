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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_sequence

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

	def test_read1 (self) :
		r = StringIO.StringIO("1 10\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 1)
		self.assert_(a[1] == 10)
		
	def test_read2 (self) :
		r = StringIO.StringIO("10 20\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 10)
		self.assert_(a[1] == 20)
		self.assert_(len(a) == 2)
	
	def test_read3 (self) :
		r = StringIO.StringIO("44 45\n")
		a = [32, 32]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 44)
		self.assert_(a[1] == 45)
		self.assert_(len(a) == 2)

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

	def test_print1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")
		
	def test_print2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 0, -1, 1)
		self.assert_(w.getvalue() == "0 -1 1\n")
	
	def test_print3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, -2934, 3939393, 10000)
		self.assert_(w.getvalue() == "-2934 3939393 10000\n")

    # -----
    # solve
    # -----

	def test_solve1 (self) :
		r = StringIO.StringIO("1 500\n500 1\n300 9088\n9088 300\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 500 144\n500 1 144\n300 9088 262\n9088 300 262\n")
	
	def test_solve2 (self) :
		r = StringIO.StringIO("1 10\n1 10\n1 10\n1 10\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n1 10 20\n1 10 20\n1 10 20\n")
	
	def test_solve3 (self) :
		r = StringIO.StringIO("128 1\n1 1\n99 100\n22 22\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "128 1 119\n1 1 1\n99 100 26\n22 22 16\n")
		
	# -----
	# sequence
	# -----
	
	def test_sequence1 (self) :
		fakeDict = {0 : 0, 1 : 1}
		a = collatz_sequence(2, fakeDict)
		self.assert_(a == 2)
	
	def test_sequence2 (self) :
		fakeDict = {0 : 0, 1 : 1}
		a = collatz_sequence(0, fakeDict)
		self.assert_(a == 0)
	
	def test_sequence3 (self) :
		fakeDict = {0 : 0, 1 : 1}
		a = collatz_sequence(1, fakeDict)
		self.assert_(a == 1)
		
	def test_sequence4 (self) :
		fakeDict = {0 : 0, 1 : 1}
		a = collatz_sequence(88, fakeDict)
		self.assert_(a == 18)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."