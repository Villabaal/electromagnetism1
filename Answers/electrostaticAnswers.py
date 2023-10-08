# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,degrees
from cmath import phase
from Answers.answers import problemAnswer
        
           
class EletricFieldAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def E(self):
        return array( cmplx2tuple( self._data['E'] ) )
    @property
    def E_magnitud(self):
        return abs( self._data['E'] )  
    @property    
    def E_theta(self):
        return degrees( phase( self._data['E'] ) )  
    def __str__ (self):
        problem_head = []
        problem_head.append( 'Campo electrico\n'+60*'*'+'\n' )
        problem_head.append( 'Carga(s):\n' )
        charges = self._data['charges']
        problem_head += [f'q{ q.id } = { q.q }C, posicionada en ({q.position.real},{q.position.imag}) m\n' 
                 for q in charges]
        problem_head.append( f'Punto en cuestión:\nP: ({ self._data["P"][0] },{ self._data["P"][1] }) m\n' )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Campo electrico\n'+60*'*'+'\n'
        head = ''.join( problem_head ) + answer_head
        E_strings = []
        E_strings.append( f'E = { self.E } V/m\n' )
        E_strings.append( f'E_magnitud = { self.E_magnitud } V/m\n' )
        E_strings.append( f'E_theta = { self.E_theta }°\n'+60*'*'+'\n\n' )
        return super().__str__( head,''.join( E_strings ) )    

class CoulombForceAnswer(problemAnswer):
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
        problem_head.append( 'Fuerza de Coulomb\n'+60*'*'+'\n' )
        problem_head.append( 'Carga pasiva:\n' )
        problem_head = ''.join( problem_head )
        q = self._data["passive_charge"]
        q_str = f'q{ q.id } = { q.q }C, posicionada en ({q.position.real},{q.position.imag}) m\n\n' 
        active_q = self._data["acting_charges"]
        active_q_str = ['Carga(s) activa(s):\n']
        active_q_str += [f'q{qa.id} = { qa.q }C, posicionada en ({qa.position.real},{qa.position.imag}) m\n' 
                 for qa in active_q]
        active_q_str = ''.join( active_q_str )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Fuerza de Coulomb\n'+60*'*'+'\n'
        head = problem_head + q_str + active_q_str + answer_head
        F_strings = []
        F_strings.append( f'F = { self.F } N\n' )
        F_strings.append( f'F_magnitud = { self.F_magnitud } N\n' )
        F_strings.append( f'F_theta = { self.F_theta }°\n'+60*'*'+'\n\n' )
        return super().__str__( head,''.join( F_strings ) )
