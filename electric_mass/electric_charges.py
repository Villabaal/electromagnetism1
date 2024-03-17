#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from electric_mass.electric import _electricMass


class electricCharge(_electricMass):    
    """Obejto de Carga Eléctrica, crea un campo eléctrico y sufre de repulsión o atracción.\n
            toma:
                - q : carga eléctrica (Coulombs)
                - p : indexable de tamaño 2
    """    
    def __init__(self,q,p):
        _electricMass.__init__(self, q, p)
        if self.q>0: self.color,self.sign = '#FF0000',1
        else: self.color,self.sign = '#0000FF',-1
    
    @property
    def q(self) -> float: return self._mass
    
    def E(self,p): return self._field(p)
        
    ## campo electrico En un punto determinado creado por la particula self
    def _field(self,p) -> complex:
        r = self._calculate_r(p)
        return (9e9)*self.q*r/abs(r)**3
    
    ##Fuerza que incide en self debido a otra carga
    def F(self,charge): 
        if not isinstance( charge,type( self ) ): 
            raise TypeError( "Debe ser una carga" )
        return -charge.q*self.E( charge.position )