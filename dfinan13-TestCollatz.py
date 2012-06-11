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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, recursiveEval

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    #recursiveEval
    # ----

        
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
        r = StringIO.StringIO("1 9\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 9)

    def test_read2 (self) :
        r = StringIO.StringIO("33 777\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  33)
        self.assert_(a[1] == 777)
      
    def test_read3 (self) :
        r = StringIO.StringIO("99999 11111\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  99999)
        self.assert_(a[1] == 11111)

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
        v = collatz_eval(210, 201)
        self.assert_(v == 89)
        
    def test_eval_6 (self) :
        v = collatz_eval(3, 75)
        self.assert_(v == 116)

    def test_eval_7 (self) :
        v = collatz_eval(9999, 5555)
        self.assert_(v == 262)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3, 75, 116)
        self.assert_(w.getvalue() == "3 75 116\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 30, 60, 113)
        self.assert_(w.getvalue() == "30 60 113\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 9999, 5555, 262)
        self.assert_(w.getvalue() == "9999 5555 262\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("1 20\n3 75\n75 20\n30 60\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 20 21\n3 75 116\n75 20 116\n30 60 113\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("9999 5555\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "9999 5555 262\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("22 363\n99 797\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "22 363 144\n99 797 171\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
