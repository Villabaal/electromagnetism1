#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:40:08 2023

@author: villabaal
"""

isReal      = lambda num:  isinstance(num, int) or isinstance(num, float) 
tuple2cmplx = lambda tup: tup[0]+1j*tup[1]
cmplx2tuple = lambda cmplx: (cmplx.real,cmplx.imag)
def Error(): raise TypeError( "Debe ser Complejo o tuple" ) 

