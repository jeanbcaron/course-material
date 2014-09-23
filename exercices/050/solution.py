# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:54:59 2014

@author: jean-baptiste
"""
a = 0
for i in range(1001):
    if (i % 3 == 0) | (i % 5 == 0):
        a = a+i
print(a)
