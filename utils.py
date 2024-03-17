#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:40:08 2023

@author: villabaal
"""
from numpy import round,ndarray
from numpy.random import normal

isReal      = lambda num:  isinstance(num, int) or isinstance(num, float) 
def tuple2cmplx( tup : tuple ) -> complex:
    return tup[0]+1j*tup[1]
cmplx2tuple = lambda cmplx: (cmplx.real,cmplx.imag)


def Error(): raise TypeError( "Debe ser Complejo o tuple" ) 

def randomPoint( loc = [0,0], scale = 1 ) -> ndarray:
    point = round( normal( loc=loc ,scale=scale ),2 )
    return (point[0],point[1])