#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from electric_mass.electric import _electricMass


class electricCurrent(_electricMass):    
    """Obejto de Carga Eléctrica, crea un campo eléctrico y sufre de repulsión o atracción.\n
            toma:
                - I : corriente eléctrica (Amperes)
                - p : indexable de tamaño 2
    """                
    def __init__(self,I,p):
        _electricMass.__init__(self, I, p)
        if self.I < 0: self.marker,self.sign = 'x',-1
        else: self.marker,self.sign = '.',1
        
    @property
    def I(self) -> float: return self._mass
    
    def B(self,p) : return self._field(p)
    
    ## campo electrico En un punto determinado creado por la particula self
    def _field(self,p) -> complex:
        r = self._calculate_r(p)
        return (4e-7)*self.I*r*1j/( 2*abs(r)**2 )
    
    ##Fuerza que incide en self debido a otra carga
    def F(self,current): 
        if not isinstance( current,type( self ) ): 
            raise TypeError( "Debe ser una corriente" )
        return -1j*current.I*self.B( current.position )
        

# base
