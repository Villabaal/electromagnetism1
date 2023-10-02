#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:40:08 2023

@author: villabaal
"""

isReal      = lambda num:  isinstance(num, int) or isinstance(num, float) 
tuple2cmplx = lambda tup: tup[0]+1j*tup[1]
cmplx2tuple = lambda cmplx: (cmplx.real,cmplx.imag)
import itertools

def Error(): raise TypeError( "Debe ser Complejo o tuple" ) 

class InstanceCounterMeta(type):
    """ Metaclass to make instance counter not share count with descendants
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._ids = itertools.count(1)