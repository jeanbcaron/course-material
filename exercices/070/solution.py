# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:25:03 2014

@author: jean-baptiste
"""

a = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    for j in range(26):
        m = a[i]
        n = a[j]
        if a[i] != a[j]:
            if i < j:
                print(m, n)
