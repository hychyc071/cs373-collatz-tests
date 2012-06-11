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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length, collatz_print_first

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
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 10)

    def test_read_3 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    # ------------
    # cycle length
    # ------------
  
    def test_cycle_length_1 (self) :
        cache = [0 for x in range(1000000)]
        v = collatz_cycle_length(1, cache)
        self.assert_(v == 1)

    def test_cycle_length_2 (self) :
        cache = [0 for x in range(1000000)]
        v = collatz_cycle_length(5, cache)
        self.assert_(v == 6)

    def test_cycle_length_3 (self) :
        cache = [0 for x in range(1000000)]
        v = collatz_cycle_length(16, cache)
        self.assert_(v == 5)
    
        

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

    def test_eval_4 (self) :
        lower = [978922, 584797, 348915, 431238, 155191, 581959, 543387, 1]
        upper = [405170, 634441, 157051, 273274, 12293, 959469, 604788, 999999]
        answer = [525, 509, 443, 449, 375, 525, 452, 525]
        for x in range (len(answer)) :
            a = collatz_eval(lower[x], upper[x])
            self.assert_(a == answer[x])


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "\n1 10 20")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 20, 30, 40)
        self.assert_(w.getvalue() == "\n20 30 40")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 10, 20)
        self.assert_(w.getvalue() == "\n100 10 20")

    # -----------
    # print first
    # -----------

    def test_print_first_1 (self) :
        w = StringIO.StringIO()
        collatz_print_first(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20")

    def test_print_first_2 (self) :
        w = StringIO.StringIO()
        collatz_print_first(w, 20, 30, 40)
        self.assert_(w.getvalue() == "20 30 40")

    def test_print_first_3 (self) :
        w = StringIO.StringIO()
        collatz_print_first(w, 100, 10, 20)
        self.assert_(w.getvalue() == "100 10 20")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174")

    def test_solve_2 (self) :
        r = StringIO.StringIO("444915 961057\n771596 768855\n398674 42676\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "444915 961057 525\n771596 768855 393\n398674 42676 443")

    def test_solve_3 (self) :
        r = StringIO.StringIO("95508 7437\n231887 82208\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "95508 7437 351\n231887 82208 443")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."