#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:00:02 2023

@author: villabaal
"""
from electric_mass.electric import _electricMass
import itertools

class InstanceCounterMeta(type):
    """ Metaclass to make instance counter not share count with descendants
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._ids = itertools.count(1)

class InstanceCounter(object, metaclass=InstanceCounterMeta):
    """ Mixin to add automatic ID generation
    """
    def __init__(self):
        self._id = next(self.__class__._ids)
    @property
    def id(self):
        return self._id
        

class electricCurrent(_electricMass,InstanceCounter):    
    """Obejto de Carga Eléctrica, crea un campo eléctrico y sufre de repulsión o atracción.\n
            toma:
                - I : corriente eléctrica (Amperes)
                - p : indexable de tamaño 2
    """                
    def __init__(self,I,p):
        _electricMass.__init__(self, I, p)
        InstanceCounter.__init__(self)
        if self.I < 0: self.marker,self.sign = 'x',-1
        else: self.marker,self.sign = '.',1
        
    @property
    def I(self): return self._mass
    
    def B(self,p): return self._field(p)
    
    ## campo electrico En un punto determinado creado por la particula self
    def _field(self,p):
        r = self._calculate_r(p)
        return (4e-7)*self.I*r*1j/( 2*abs(r)**2 )
    
    ##Fuerza que incide en self debido a otra carga
    def F(self,current): 
        if not isinstance( current,type( self ) ): 
            raise TypeError( "Debe ser una corriente" )
        return -1j*current.I*self.B( current.position )
        

# base
