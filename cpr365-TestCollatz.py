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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_recursive_cache

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
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
    def test_read_2 (self) :
        r = StringIO.StringIO("20 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  20)
        self.assert_(a[1] == 10)
    def test_read_3 (self) :
        r = StringIO.StringIO("1000 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1000)
        self.assert_(a[1] == 1)
    def test_read_4 (self) :
        r = StringIO.StringIO("9155 77894\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  9155)
        self.assert_(a[1] == 77894)

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
        
    # ----
    # recursive_cache
    # ----

    def test_recursive_cache_1 (self) :
        i = collatz_recursive_cache(500)
        self.assert_(i == 111)

    def test_recursive_cache_2 (self) :
        i = collatz_recursive_cache(78946)
        self.assert_(i == 77)

    def test_recursive_cache_3 (self) :
        i = collatz_recursive_cache(90000)
        self.assert_(i == 165)

    def test_recursive_cache_4 (self) :
        i = collatz_recursive_cache(8989)
        self.assert_(i == 79)
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 60997, 61209, 255)
        self.assert_(w.getvalue() == "60997 61209 255\n")
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 372363, 372512, 242)
        self.assert_(w.getvalue() == "372363 372512 242\n")
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 328276, 329071, 335)
        self.assert_(w.getvalue() == "328276 329071 335\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("393745 394409\n23545 24211\n288287 288364\n250177 250926\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "393745 394409 361\n23545 24211 251\n288287 288364 327\n250177 250926 332\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("10605 10901\n37424 37823\n810943 811521\n477452 477565\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10605 10901 255\n37424 37823 306\n810943 811521 344\n477452 477565 245\n")
        
    def test_solve_4 (self) :
        r = StringIO.StringIO("60997 61209\n564286 564757\n489814 490409\n149229 149847\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "60997 61209 255\n564286 564757 284\n489814 490409 307\n149229 149847 326\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
