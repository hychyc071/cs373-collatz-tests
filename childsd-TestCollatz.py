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
        
    def test_read_1 (self) :
        r = StringIO.StringIO("1 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1000000)
    
    def test_read_2 (self) : 
        r = StringIO.StringIO("999999 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] == 1000000)

    def test_read_3 (self) :
        r = StringIO.StringIO("1000001 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1000001)
        self.assert_(a[1] == 1)

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
        v = collatz_eval(999999, 999999)
        self.assert_(v == 259)
    
    def test_eval_6 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
    
    def test_eval_7 (self) :
        v = collatz_eval(837800, 999999)
        self.assert_(v == 507)
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 1, 1000000)
        self.assert_(w.getvalue() == "0 1 1000000\n")
    
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000002, 1000000, 1000001)
        self.assert_(w.getvalue() == "1000002 1000000 1000001\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 1, 0)
        self.assert_(w.getvalue() == "0 1 0\n")
        
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_1 (self) :
        r = StringIO.StringIO("1 999999\n999998 999999\n999 1000\n100000 900000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 999999 525\n999998 999999 259\n999 1000 112\n100000 900000 525\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 2\n2 3\n3 4\n4 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n2 3 8\n3 4 8\n4 5 6\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 10\n10 100\n100 1000\n1000 10000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n10 100 119\n100 1000 179\n1000 10000 262\n")
        
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."