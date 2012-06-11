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

    def test_read_2 (self) :
        r = StringIO.StringIO("5 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] == 1)

    def test_read_3 (self) :
        r = StringIO.StringIO("1 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1000)

    def test_read_4 (self) :
        r = StringIO.StringIO("5000 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5000)
        self.assert_(a[1] == 1000)

    def test_read_5 (self) :
        r = StringIO.StringIO("100 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 1000000)

    def test_read_6 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)


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
        v = collatz_eval(1, 1000000)
        self.assert_(v == 525)

    def test_eval_6 (self) :
        v = collatz_eval(90, 1)
        self.assert_(v == 116)

    def test_eval_7 (self) :
        v = collatz_eval(3, 74033)
        self.assert_(v == 51)

    def test_eval_8 (self) :
        v = collatz_eval(278, 24)
        self.assert_(v == 128)

    def test_eval_9 (self) :
        v = collatz_eval(1000000, 1)
        self.assert_(v == 525)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 1, 2)
        self.assert_(w.getvalue() == "100 1 2\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000000, 1, 0)
        self.assert_(w.getvalue() == "1000000 1 0\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 999999, 10, 20)
        self.assert_(w.getvalue() == "999999 10 20\n")

    def test_print_5 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1123123, 1123123, 1123123)
        self.assert_(w.getvalue() == "1123123 1123123 1123123\n")

    def test_print_6 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 0, 0)
        self.assert_(w.getvalue() == "0 0 0\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("8310 1622\n5562 8057\n4015 8009\n9314 3405\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "8310 1622 262\n5562 8057 262\n4015 8009 262\n9314 3405 262\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("300 644\n929 847\n174 815\n8310 1622\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "300 644 144\n929 847 179\n174 815 171\n8310 1622 262\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("109454 106340\n978468 859997\n302513 781783\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "109454 106340 323\n978468 859997 507\n302513 781783 509\n")

    def test_solve_5 (self) :
        r = StringIO.StringIO("772718 801813\n595598 246937\n650921 603965\n573044 608117\n967492 826419\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "772718 801813 468\n595598 246937 470\n650921 603965 509\n573044 608117 434\n967492 826419 525\n")

    def test_solve_6 (self) :
        r = StringIO.StringIO("1 1000000\n9 1\n1 90\n1000000 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000000 525\n9 1 20\n1 90 116\n1000000 1 525\n")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
