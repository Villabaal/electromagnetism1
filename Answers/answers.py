# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,degrees
from cmath import phase



class problemAnswer:
    _instance_n = 0
    def __init__(self,data):
        self._data = data
        problemAnswer._instance_n += 1
        self.id = problemAnswer._instance_n
            
    @property
    def fig(self):
        return self._data['fig']
    @property
    def splot(self):
        return self._data['splot']    
    @property
    def r(self):
        return array( [  cmplx2tuple( ri ) for ri in self._data['r'] ] )
    @property
    def distance(self):
        return array([ abs(ri) for ri in self._data['r'] ])
    @property
    def r_theta(self):
        return array([ degrees( phase( ri ) )  for ri in self._data['r'] ])
    @property
    def ru(self):
        return array([  cmplx2tuple( ri/abs(ri) )  for ri in self._data['r'] ])
    
    def __str__ ( self, head, body ): #to do, str atribute to print
        start = 60*'*'+f'\nDatos del Problema {self.id}: ' 
        r_strings = []
        r_strings.append( [ f'r{i+1} = {self.r[i]} m' for i in range( len(self.r) ) ] )
        r_strings.append( [ f'distance{i+1} = {self.distance[i] } m' for i in range( len(self.r) ) ] )
        r_strings.append( [ f'theta{i+1} = {self.r_theta[i]}°' for i in range( len(self.r) ) ] )
        r_strings.append( [ f'ru{i+1} = {self.ru[i]}' for i in range( len(self.r) ) ] )
        r_string = ''.join ( [ ''.join ( [ f'{ lst[i] }\n' for lst in r_strings ] )+'\n' 
                    for i in range( len(self.r) ) ] )
        return ''.join( [ start, head, r_string, body ] )
    
    