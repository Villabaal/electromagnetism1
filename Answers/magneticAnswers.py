# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,degrees
from cmath import phase
from Answers.answers import problemAnswer


class MagneticFieldAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def B(self):
        return array( cmplx2tuple( self._data['B'] ) )
    @property
    def B_magnitud(self):
        return abs( self._data['B'] )  
    @property    
    def B_theta(self):
        return degrees( phase( self._data['B'] ) )  
    def __str__ (self):
        problem_head = []
        problem_head.append( 'Campo magnetico\n'+60*'*'+'\n' )
        problem_head.append( 'Corrientes(s):\n' )
        currents = self._data['currents']
        problem_head += [f'I{ i.id } = { i.I }A, posicionada en ({i.position.real},{i.position.imag}) m\n' 
                 for i in currents]
        problem_head.append( f'Punto en cuestión:\nP: ({ self._data["P"][0] },{ self._data["P"][1] }) m\n' )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Campo magnetico\n'+60*'*'+'\n'
        head = ''.join( problem_head ) + answer_head
        B_strings = []
        B_strings.append( f'B = { self.B } T\n' )
        B_strings.append( f'B_magnitud = { self.B_magnitud } T\n' )
        B_strings.append( f'B_theta = { self.B_theta }°\n'+60*'*'+'\n\n' )
        return super().__str__( head,''.join( B_strings ) )    

class MagneticForceAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def F(self):
        return array( cmplx2tuple( self._data['F'] ) )
    @property
    def F_magnitud(self):
        return abs( self._data['F'] )   
    @property    
    def F_theta(self):
        return degrees( phase( self._data['F'] ) )  
    
    def __str__ (self):
        problem_head = []
        problem_head.append( 'Fuerza de magnetica\n'+60*'*'+'\n' )
        problem_head.append( 'Corriente pasiva:\n' )
        problem_head = ''.join( problem_head )
        i = self._data["passive_I"]
        I_str = f'I{ i.id } = { i.I }A, posicionada en ({i.position.real},{i.position.imag}) m\n\n' 
        active_I = self._data["acting_currents"]
        active_I_str = ['Corriente(s) activa(s):\n']
        active_I_str += [f'I{Ia.id} = { Ia.I }A, posicionada en ({Ia.position.real},{Ia.position.imag}) m\n' 
                 for Ia in active_I]
        active_I_str = ''.join( active_I_str )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Fuerza de Coulomb\n'+60*'*'+'\n'
        head = problem_head + I_str + active_I_str + answer_head
        F_strings = []
        F_strings.append( f'F = { self.F } N\n' )
        F_strings.append( f'F_magnitud = { self.F_magnitud } N\n' )
        F_strings.append( f'F_theta = { self.F_theta }°\n'+60*'*'+'\n\n' )
        return super().__str__( head,''.join( F_strings ) )
