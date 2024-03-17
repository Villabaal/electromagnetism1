# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,ndarray
from matplotlib.figure import Figure



class problemAnswer:
    def __init__(self,data):
        self._data = data
            
    @property
    def fig(self) -> Figure:
        return self._data['fig']
    @property
    def r(self) -> ndarray:
        return array( [  cmplx2tuple( ri ) for ri in self._data['r'] ] )
    @property
    def r2(self) -> ndarray:
        return array([ abs(ri)**2 for ri in self._data['r'] ])
    
    def __str__ ( self, head: str, body: str )->str: #to do, str atribute to print
        start = 60*'*'+f'\nDatos del Problema: ' 
        r_strings = []
        r_strings.append( [ f'r{i+1} = {self.r[i]} m' for i in range( len(self.r) ) ] )
        r_strings.append( [ f'|r{i+1}|² = {self.r2[i]} m²' for i in range( len(self.r) ) ] )
        r_string = ''.join ( [ ''.join ( [ f'{ lst[i] }\n' for lst in r_strings ] )+'\n' 
                    for i in range( len(self.r) ) ] )
        return ''.join( [ start, head, r_string, body ] )
    
    