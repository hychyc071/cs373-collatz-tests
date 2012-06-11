#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.py.out
    % python TestCollatz.py &> TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_getCycLen, collatz_print, collatz_solve

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
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 200)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  201)
        self.assert_(a[1] == 210)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  900)
        self.assert_(a[1] == 1000)
    
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

    # -------
    # my eval
    # -------
    
    def test_my_eval_1 (self) :
        v = collatz_eval(1, 666)
        self.assert_(v == 145)

    def test_my_eval_2 (self) :
        v = collatz_eval(1, 999)
        self.assert_(v == 179)

    def test_my_eval_3 (self) :
        v = collatz_eval(128, 256)
        self.assert_(v == 128)

    # ---------
    # getCycLen
    # ---------
    
    def test_getCycLen_1 (self) :
        v = collatz_getCycLen(1)
        self.assert_(v == 1)

    def test_getCycLen_2 (self) :
        v = collatz_getCycLen(5)
        self.assert_(v == 6)

    def test_getCycLen_3 (self) :
        v = collatz_getCycLen(10)
        self.assert_(v == 7)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")
    
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_1 (self) :
        r = StringIO.StringIO("774943 258817\n403764 106371\n137050 675589\n473351 155848\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "774943 258817 509\n403764 106371 443\n137050 675589 509\n473351 155848 449\n")
    
    def test_solve_2 (self) :
        r = StringIO.StringIO("921039 198236\n75893 383240\n707043 600158\n495152 205986\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "921039 198236 525\n75893 383240 443\n707043 600158 509\n495152 205986 449\n")
    
    def test_solve_3 (self) :
        r = StringIO.StringIO("669479 200077\n362042 881315\n648405 348323\n259830 568259\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "669479 200077 509\n362042 881315 525\n648405 348323 509\n259830 568259 470\n")
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
