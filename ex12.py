#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:59:48 2020

@author: raphael
"""

max = 100


def prime(max):
    
    list_prime = []
    l = list(range(max + 1))
    l[1] = 0
    
    
    
    
    i = 2
    while i*i <= max:
        if l[i] != 0:
            
            for j in range(2 * i, max + 1, i):
                l[j] = 0
                
        i += 1
        
    for i in range(max):
        if l[i] != 0:
            list_prime.append(l[i])
        
        
        
    return list_prime

print(prime(max))
print(len(prime(max))) 










"""print(list(range(100)))  """             