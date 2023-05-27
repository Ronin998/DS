#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 12:11:43 2023

@author: saurabhpalande
"""

myfile = open('/Users/saurabhpalande/Data Science/DS/Saurabh.txt', 'a+')

myfile.write('This is written using spyder /n')

myfile.seek(0)

print(myfile.readlines())

myfile.close()