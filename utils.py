#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:40:08 2023

@author: villabaal
"""
from random import uniform

isReal      = lambda num:  isinstance(num, int) or isinstance(num, float) 
tuple2cmplx = lambda tup: tup[0]+1j*tup[1]
cmplx2tuple = lambda cmplx: (cmplx.real,cmplx.imag)


def Error(): raise TypeError( "Debe ser Complejo o tuple" ) 

def randomPoint( x_lim = (-3,3), y_lim = (-3,3) ):
    return ( round( uniform( x_lim[0], x_lim[1] ),3 ) , round( uniform( y_lim[0] , y_lim[1] ) ,3 ) ) 