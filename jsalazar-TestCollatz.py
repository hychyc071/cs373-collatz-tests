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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cyLength

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
        
    def test_read_2 (self) :
        r = StringIO.StringIO("45 52\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  45)
        self.assert_(a[1] == 52)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("203 395\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  203)
        self.assert_(a[1] == 395)

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
    # cyLength
    # -----
    
    def test_cylength_1(self) :
        a = cyLength(6)
        self.assert_( a == 9)
    
    def test_cylength_2(self) :
        a = cyLength(567)
        self.assert_( a == 62)
    
    def test_cylength_3(self) :
        a = cyLength(304039)
        self.assert_( a == 58)
        
    

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 21, 94, 116)
        self.assert_(w.getvalue() == "21 94 116\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 90, 98, 119)
        self.assert_(w.getvalue() == "90 98 119\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("21 94\n43 146\n52 429\n89 371\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "21 94 116\n43 146 122\n52 429 144\n89 371 144\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("34 306\n32 78\n62 160\n60 279\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "34 306 128\n32 78 116\n62 160 122\n60 279 128\n")
        

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."