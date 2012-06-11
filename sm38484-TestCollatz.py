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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, eval_cycle

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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)
 
    def test_read_lowerbound (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)
        
    def test_read_middle1 (self) :
        r = StringIO.StringIO("499999 500000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 499999)
        self.assert_(a[1] == 500000)
   
    def test_read_middle2 (self) :
        r = StringIO.StringIO("500000 499999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 500000)
        self.assert_(a[1] == 499999)
        
    def test_read_range (self) :
        r = StringIO.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 999999)
     
    def test_read_end (self) :
        r = StringIO.StringIO("999999 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 999999)
        self.assert_(a[1] == 999999)
        
        

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)
    
    def test_eval_one(self):
        v = collatz_eval(1,1)
        self.assert_(v==1)
   
    def test_eval_two(self):
        v = collatz_eval(10,1)
        self.assert_(v==20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)
        
    def test_eval_swap(self) :
        v = collatz_eval(9, 2)
        self.assert_(v == 20)
        
    def test_eval_mid (self) :
        v = collatz_eval(499999, 500000)
        self.assert_(v == 258)
        
    def test_eval_mid2 (self) :
        v = collatz_eval(500000, 499999)
        self.assert_(v == 258)
        
    def test_eval_edgehigh (self) :
        v = collatz_eval(999999, 999999)
        self.assert_(v == 259)
        
    def test_eval_edgehigh (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
   
     # ----
    # eval_cycle 
    # ----

    def test_eval_cycle1 (self) :
        v = eval_cycle(1)
        self.assert_(v == 1) 
        
    def test_eval_cycle2 (self) :
        v = eval_cycle(27)
        self.assert_(v == 112) 
        
    def test_eval_cycle3 (self) :
        v = eval_cycle(16)
        self.assert_(v == 5)       
        
      
    
    
        

        

        
 

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")\
        
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")\
        
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")\
        
    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 1, 525)
        self.assert_(w.getvalue() == "999999 1 525\n")\
        
    def test_print5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 499999, 500000, 258)
        self.assert_(w.getvalue() == "499999 500000 258\n")\
        
    def test_print6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 999999, 259)
        self.assert_(w.getvalue() == "999999 999999 259\n")\
        
    def test_print7 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")\
        
        
        


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve2 (self) :
        r = StringIO.StringIO("1 1\n1 999999\n499999 500000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 999999 525\n499999 500000 258\n")
        
    def test_solve3 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")
        
    def test_solve4 (self) :
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
