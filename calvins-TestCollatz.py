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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc, collatz_cache, collatz_range_cache, collatz_cache_calc, collatz_range_eval

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

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10, None,None)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200, None,None)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210, None,None)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000, None,None)
        self.assert_(v == 174)
    """
    # eager cache
    def test_eval_1b (self) :
        cache = []
        collatz_cache(cache)
        v = collatz_eval(1, 10, cache)
        self.assert_(v == 20)

    def test_eval_2b (self) :
        cache = []
        collatz_cache(cache)
        v = collatz_eval(100, 200, cache)
        self.assert_(v == 125)

    def test_eval_3b (self) :
        cache = []
        collatz_cache(cache)
        v = collatz_eval(201, 210, cache)
        self.assert_(v == 89)

    def test_eval_4b (self) :
        cache = []
        collatz_cache(cache)
        v = collatz_eval(900, 1000, cache)
        self.assert_(v == 174)
    """
    # eager range cache
    def test_eval_1c (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        v = collatz_eval(1, 10, lazy_cache, cache, 99)
        self.assert_(v == 20)

    def test_eval_2c (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        v = collatz_eval(10100, 15150, lazy_cache, cache, 99)
        self.assert_(v == 276)

    def test_eval_3c (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        v = collatz_eval(10101, 668811, lazy_cache, cache, 99)
        self.assert_(v == 509)

    def test_eval_4c (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        v = collatz_eval(545455, 636363, lazy_cache, cache, 99)
        self.assert_(v == 509)

    # ----------
    # range_eval
    # ----------

    def test_range_eval_1 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        v = collatz_range_eval(16, 39, lazy_cache, cache, 111111)
        self.assert_(v == 112)

    def test_range_eval_2 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        v = collatz_range_eval(19, 39, lazy_cache, cache, 111111)
        self.assert_(v == 112)
        
    def test_range_eval_3 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        v = collatz_range_eval(16, 36, lazy_cache, cache, 111111)
        self.assert_(v == 112)

    def test_range_eval_4 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        v = collatz_range_eval(19, 36, lazy_cache, cache, 111111)
        self.assert_(v == 112)

    # ----
    # calc
    # ----

    def test_calc_1 (self) :
        n = collatz_calc(5)
        self.assert_(n == 6)

    def test_calc_2 (self) :
        n = collatz_calc(1)
        self.assert_(n == 1)

    def test_calc_3 (self) :
        n = collatz_calc(7)
        self.assert_(n == 17)

    # --------------
    # cache_calc
    # --------------

    def test_cache_calc_1 (self) :
        cache = [0]*1000000
        n = collatz_cache_calc(5, cache)
        self.assert_(n == 6)
        self.assert_(cache[5] == 6)

    def test_cache_calc_2 (self) :
        cache = [0]*1000000
        n = collatz_cache_calc(1, cache)
        self.assert_(n == 1)
        self.assert_(cache[5] == 0)

    def test_cache_calc_3 (self) :
        cache = [0]*1000000
        n = collatz_cache_calc(7, cache)
        self.assert_(n == 17)
        self.assert_(cache[5] == 6)

    # -----
    # cache
    # -----
    """
    def test_cache_1 (self) :
        cache = []
        collatz_cache(cache)
        self.assert_(cache[5] == 6)

    def test_cache_2 (self) :
        cache = []
        collatz_cache(cache)
        self.assert_(cache[1] == 1)

    def test_cache_3 (self) :
        cache = []
        collatz_cache(cache)
        self.assert_(cache[7] == 17)
    """

    # -----------
    # range_cache
    # -----------

    def test_range_cache_1 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        self.assert_(len(cache) == 99)

    def test_range_cache_2 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        self.assert_(cache[0] == 262)

    def test_range_cache_3 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 99)
        self.assert_(cache[7] == 351)

    def test_range_cache_4 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        self.assert_(len(cache) == 111111)

    def test_range_cache_5 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        self.assert_(cache[0] == 20)

    def test_range_cache_6 (self) :
        cache = []
        lazy_cache = [0]*1000000
        collatz_range_cache(lazy_cache, cache, 111111)
        self.assert_(cache[2] == 112)

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

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
