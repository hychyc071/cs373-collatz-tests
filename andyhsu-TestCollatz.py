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

from Collatz import collatz_read, collatz_cycles, collatz_cache_init, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

	def test_read_1 (self) :		# Accepted string
		r = StringIO.StringIO("1 10\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)

	def test_read_2 (self) :		# Excessive string
		r = StringIO.StringIO("15 12 junk junk morejunk\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] == 15)
		self.assert_(a[1] == 12)

	def test_read_4 (self) :		# Empty string
		r = StringIO.StringIO("")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == False)
		self.assert_(a[0] == 0)
		self.assert_(a[1] == 0)


	# ------
	# cycles
	# ------

	def test_cycles_1 (self) :	# No cache
		cache = [0]
		cachelen = 0
		v = collatz_cycles(cache, cachelen, 1)
		self.assert_(v == 1)

	def test_cycles_2 (self) :	# Using cache
		cache = [0, 1, 2, 0, 3, 0, 0, 0, 4]
		cachelen = 9
		v = collatz_cycles(cache, cachelen, 5)
		self.assert_(v == 6)

	def test_cycles_3 (self) : 	# Normal
		cache = [0, 1, 2, 0, 3, 0, 0, 0, 4]
		cachelen = 9
		v = collatz_cycles(cache, cachelen, 7)
		self.assert_(v == 17)

	def test_cycles_4 (self) :	# Extensive calculation
		cache = [0, 1, 2, 0, 3, 0, 0, 0, 4]
		cachelen = 9
		v = collatz_cycles(cache, cachelen, 27)
		self.assert_(v == 112)

	def test_cycles_5 (self) :	# Extensive calculation
		cache = [0, 1, 2, 0, 3, 0, 0, 0, 4]
		cachelen = 9
		v = collatz_cycles(cache, cachelen, 60975)
		self.assert_(v == 335)

	def test_cycles_6 (self) :	# Extensive calculation
		cache = [0, 1, 2, 0, 3, 0, 0, 0, 4]
		cachelen = 9
		v = collatz_cycles(cache, cachelen, 704511)
		self.assert_(v == 243)


	# ----------

	# cache_init
	# ----------

	def test_cache_init_1 (self) :
		n = 1
		v = collatz_cache_init(n)
		self.assert_(v == [0])

	def test_cache_init_2 (self) :
		n = 10
		v = collatz_cache_init(n)
		self.assert_(v == [0, 1, 2, 0, 3, 0, 0, 0, 4, 0])

	def test_cache_init_3 (self) :
		n = 4
		v = collatz_cache_init(n)
		self.assert_(v == [0, 1, 2, 0])


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

	def test_eval_5 (self) :	# Size 1 range
		v = collatz_eval(10, 10)
		self.assert_(v == 7)

	def test_eval_6 (self) :	# Reverse range
		v = collatz_eval(200, 100)
		self.assert_(v == 125)

	def test_eval_7 (self) :	# Size 1 again
		v = collatz_eval(27, 27)
		self.assert_(v == 112)

	def test_eval_8 (self) :	# Reverse range
		v = collatz_eval(1000, 900)
		self.assert_(v == 174)

	

    # -----
    # print
    # -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, "i", "like", "turtles")
		self.assert_(w.getvalue() == "i like turtles\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 25, 1, 20)
		self.assert_(w.getvalue() == "25 1 20\n")

	def test_print_4 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 90000000000000, 10, 2101540)
		self.assert_(w.getvalue() == "90000000000000 10 2101540\n")

    # -----
    # solve
    # -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_2 (self) :	# Empty input
		r = StringIO.StringIO("")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "")

	def test_solve_3 (self) :
		r = StringIO.StringIO("999999 999999\n999999 1\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "999999 999999 259\n999999 1 525\n")

	def test_solve_4 (self) :	# 1's only
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











