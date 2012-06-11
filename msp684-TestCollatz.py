#!/usr/bin/env python

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, is_even, lazy_cache

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
        r = StringIO.StringIO("23435 5678\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  23435)
        self.assert_(a[1] ==  5678)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("234234 45646\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  234234)
        self.assert_(a[1] ==  45646)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("1 11\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  11)

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
        collatz_print(w, 456, 789, 22)
        self.assert_(w.getvalue() == "456 789 22\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 666, 666, 666)
        self.assert_(w.getvalue() == "666 666 666\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 234, 465, 123345)
        self.assert_(w.getvalue() == "234 465 123345\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self) :
        r = StringIO.StringIO("30 40\n50 60\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "30 40 107\n50 60 113\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("10000 10000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10000 10000 30\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("123 456\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "123 456 144\n")
        
    # ----
    # is_even
    # ----
    
    def test_is_even (self):
        a = [2, 4, 6, 8, 10]
        for x in a:
            self.assert_(is_even(x))
            
    def test_is_even_2 (self):
        a = [101, 103, 105]
        for x in a:
            self.assert_(not is_even(x))
            
    def test_is_even_3 (self):
        b = 6
        self.assert_(is_even(b))
        b += 1
        self.assert_(not is_even(b))
        
    # ----
    # lazy_cache
    # ----
    
    def test_lazy_cache (self):
        l = [0]*1000001
        l[1] = 1
        lazy_cache(1, 10, l)
        assert l[5] == 6
    
    def test_lazy_cache_2 (self):
        l = [0]*1000001
        l[1] = 1
        lazy_cache(10, 100, l)
        assert l[50] == 25
    
    def test_lazy_cache_3 (self):
        l = [0]*1000001
        l[1] = 1
        lazy_cache(100, 10000, l)
        assert l[5000] == 29
    

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."