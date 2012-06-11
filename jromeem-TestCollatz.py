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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, do_bin, bin_collatz, check_meta, max_collatz

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
        r = StringIO.StringIO("382 948\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  382)
        self.assert_(a[1] ==  948)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("999999 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999999)
        self.assert_(a[1] ==  10)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("22289 199\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  22289)
        self.assert_(a[1] ==  199)

    # ----
    # do_bin
    # ----

    def test_do_bin_1 (self):
        b = do_bin(3)
        self.assert_(b == "11")

    def test_do_bin_1 (self):
        b = do_bin(2344)
        self.assert_(b == "100100101000")

    def test_do_bin_1 (self):
        b = do_bin(777)
        self.assert_(b == "1100001001")

    # ----
    # bin_collatz
    # ----
    
    def test_bin_collatz_1 (self):
        c = bin_collatz(9)
        self.assert_(c == 20)
        
    def test_bin_collatz_2 (self):
        c = bin_collatz(871)
        self.assert_(c == 179)
        
    def test_bin_collatz_3 (self):
        c = bin_collatz(999999)
        self.assert_(c == 259)

    # ----
    # check_meta
    # ----
    def test_check_meta_1 (self):
        m = check_meta(range(1, 10))
        self.assert_(m == 20)
        
    def test_check_meta_2 (self):
        m = check_meta(range(23443, 48230))
        self.assert_(m == 324)
        
    def test_check_meta_3 (self):
        m = check_meta(range(1, 999999))
        self.assert_(m == 525)

    # ----
    # max_collatz
    # ----
    def dummy_function (num):
        return 123
    
    def test_max_collatz_1 (self):
        x = max_collatz(dummy_function, 1, 1)
        self.assert_(x == 123)

    def test_max_collatz_1 (self):
        x = max_collatz(dummy_function, 1, 10)
        self.assert_(x == 9)

    def test_max_collatz_1 (self):
        x = max_collatz(bin_collatz, 1, 999999)
        self.assert_(x == 525)        
    
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

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 34, 0, 234)
        self.assert_(w.getvalue() == "34 0 234\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 7, 7, 7)
        self.assert_(w.getvalue() == "7 7 7\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 235, 132)
        self.assert_(w.getvalue() == "999999 235 132\n")

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
