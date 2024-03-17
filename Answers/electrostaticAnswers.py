# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,ndarray
from Answers.answers import problemAnswer
from electric_mass import electricCharge
        
           
class EletricFieldAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def E(self) -> ndarray:
        return array( cmplx2tuple( self._data['E'] ) )
    @property
    def E_magnitud(self) -> float:
        return abs( self._data['E'] )  
    @property
    def Ei(self) -> ndarray:
        return array( [  cmplx2tuple( _field ) for _field in self._data['Ei'] ] )
    @property
    def Ei_mag(self) -> ndarray:
        return array([ abs(B) for B in self._data['Ei'] ])    
     
    def __str__ (self) -> str:
        problem_head = []
        problem_head.append( 'Campo electrico\n'+60*'*'+'\n' )
        problem_head.append( 'Carga(s):\n' )
        charges: list[electricCharge] = self._data['charges']
        problem_head += [f'q{ id+1 } = { q.q*1e6 } uC, posicionada en ({q.position.real},{q.position.imag}) m\n' 
                 for id,q in enumerate(charges)]
        problem_head.append( f'Punto en cuestión:\nP: ({ self._data["P"][0] },{ self._data["P"][1] }) m\n' )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Campo electrico\n'+60*'*'+'\n'
        head = ''.join( problem_head ) + answer_head
        
        Ei_string = ''.join ( [ f'E{i+1} = {self.Ei[i] } V/m\n\n' for i in range( len(self.Ei) ) ] )
        
        E_strings = []
        E_strings.append( f'E = { self.E } V/m\n' )
        E_strings.append( f'E_magnitud = { self.E_magnitud } V/m\n' )
        E_strings.append( 60*'*'+'\n\n' )
        return super().__str__( head,Ei_string + ''.join( E_strings ) )    

class CoulombForceAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def F(self) -> ndarray:
        return array( cmplx2tuple( self._data['F'] ) )
    @property
    def F_magnitud(self) -> float:
        return abs( self._data['F'] )   
    @property
    def Fi(self) -> ndarray:
        return array( [  cmplx2tuple( _field ) for _field in self._data['Fi'] ] )
    @property
    def Fi_mag(self) -> ndarray:
        return array([ abs(B) for B in self._data['Fi'] ])     
    
    def __str__ (self) -> str:
        problem_head = []
        problem_head.append( 'Fuerza de Coulomb\n'+60*'*'+'\n' )
        problem_head.append( 'Carga pasiva:\n' )
        problem_head = ''.join( problem_head )
        Pid: int = self._data["passive_charge"][0]
        q: electricCharge = self._data["passive_charge"][1]
        q_str = f'q{ Pid } = { q.q*1e6 }uC, posicionada en ({q.position.real},{q.position.imag}) m\n\n' 
        active_q: dict[int,electricCharge] = self._data["acting_charges"]
        active_q_str = ['Carga(s) activa(s):\n']
        active_q_str += [f'q{id} = { qa.q*1e6 } uC, posicionada en ({qa.position.real},{qa.position.imag}) m\n' 
                 for id,qa in active_q.items()]
        active_q_str = ''.join( active_q_str )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Fuerza de Coulomb\n'+60*'*'+'\n'
        head = problem_head + q_str + active_q_str + answer_head
        
        Fi_string = ''.join ( [ f'F{i+1} = {self.Fi[i]*1e6 } uN\n\n' for i in range( len(self.Fi) ) ] )
        
        F_strings = []
        F_strings.append( f'F = { self.F*1e6 } uN\n' )
        F_strings.append( f'F_magnitud = { self.F_magnitud*1e6 } uN\n' )
        F_strings.append( 60*'*'+'\n\n' )
        return super().__str__( head,Fi_string+''.join( F_strings ) )
