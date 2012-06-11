#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2011
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python chrisv-TestCollatz.py > chrisv-TestCollatz.py.out
    % chmod ugo+x chrisv-TestCollatz.py
    % chrisv-TestCollatz.py > chrisv-TestCollatz.py.out
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

    def test_read2 (self) :
        r = StringIO.StringIO("1 10 11\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
         
    def test_read3 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] ==  0)
        self.assert_(a[1] == 0)
               
    # ----
    # eval
    # ----

    def test_eval1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)
        
    def test_eval5 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval6 (self) :
        v = collatz_eval(10, 110)
        self.assert_(v == 119)

    def test_eval7 (self) :
        v = collatz_eval(100, 50)
        self.assert_(v == 119)

    def test_eval8 (self) :
        v = collatz_eval(1, 1000)
        self.assert_(v == 179)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print (self) :
            w = StringIO.StringIO()
            collatz_print(w, 1, 100, 119)
            self.assert_(w.getvalue() == "1 100 119\n")


    def test_print (self) :
            w = StringIO.StringIO()
            collatz_print(w, 100, 50, 119)
            self.assert_(w.getvalue() == "100 50 119\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
 
    def test_solve2(self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_solve4 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")


    def test_solve5 (self) :
        r = StringIO.StringIO("1 4\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 4 8\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
