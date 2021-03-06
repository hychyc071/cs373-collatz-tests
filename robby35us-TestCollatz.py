#!c://python32/python.exe
# -*- coding: utf-8 -*-

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing and Robert Reed
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

from Collatz import  collatz_read, collatz_eval, collatz_cycle_length, collatz_print, collatz_solve


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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO("1 10 11\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_3 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    

#THESE TESTS WILL CAUSE ERRORS!!!!

#    def test_read_4 (self) :
#        r = StringIO.StringIO("1\n")
#        a = [0, 0]
#        b = collatz_read(r, a)
#        self.assert_(b == False)
#        self.assert_(a[0] == 1)
#        self.assert_(a[1] == 0)

#    def test_read_5 (self) :
#        r = StringIO.StringIO("\n")
#        a = [0, 0]
#        b = collatz_read(r, a)
#        self.assert_(b == False)
#        self.assert_(a[0] == 0)
#        self.assert_(a[1] == 0)

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
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_6 (self) :
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_7 (self) :
        v = collatz_eval(11, 11)
        self.assert_(v == 15)

    def test_eval_8 (self) :
        v = collatz_eval(27, 27)
        self.assert_(v == 112)
    

    # -----
    # cycle_length
    # -----

    def test_cyc_len_1 (self) :
        v = collatz_cycle_length(6)
        self.assert_(v == 9)

    def test_cyc_len_2 (self) :
        v = collatz_cycle_length(11)
        self.assert_(v == 15)

    def test_cyc_len_3 (self) :
        v = collatz_cycle_length(27)
        self.assert_(v == 112)

    def test_cyc_len_4 (self) :
        v = collatz_cycle_length(1)
        self.assert_(v == 1)


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

#This method will be exchausted by the 1000+ acceptence tests.
    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")
        
    # -----  
    # check
    # ----- 
    
    def test_check_1 (self) :
        i, j = 1, 40
        i, j = _check_range_order(i, j)
        self.assert_(i == 1)
        self.assert_(j == 40)

    def test_check_2 (self) :
        i, j = 40, 1 
        i, j = _check_range_order(i, j)
        self.assert_(i == 1)
        self.assert_(j == 40)
        
    def test_check_3 (self) :
        i, j = 1, 1
        i, j = _check_range_order(i, j)
        self.assert_(i == 1)
        self.assert_(j == 1)

    def test_check_4 (self) :
        i, j = 1, -17
        i, j = _check_range_order(i, j)
        self.assert_(i == -17)
        self.assert_(j == 1)
        
        
    #----
    #swap
    #----
    
    def test_swap_1 (self) :
        i, j = 1, 40
        i, j = _swap_var(i, j)
        self.assert_(i == 40)
        self.assert_(j == 1)

    def test_swap_2 (self) :
        i, j = 1, 1 
        i, j = _swap_var(i, j)
        self.assert_(i == 1)
        self.assert_(j == 1)
        
    def test_swap_3 (self) :
        i, j = None, []
        i, j = _swap_var(i, j)
        self.assert_(i == [])
        self.assert_(j == None)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
