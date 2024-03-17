# -*- coding: utf-8 -*-
from utils import cmplx2tuple
from numpy import array,ndarray
from Answers.answers import problemAnswer
from electric_mass import electricCurrent


class MagneticFieldAnswer(problemAnswer):
    def __init__(self,**kargs):
        super().__init__(kargs)
    @property
    def B(self) -> ndarray:
        return array( cmplx2tuple( self._data['B'] ) )
    @property
    def B_mag(self) -> float:
        return abs( self._data['B'] ) 
    @property
    def Bi(self) -> ndarray:
        return array( [  cmplx2tuple( _field ) for _field in self._data['Bi'] ] )
    @property
    def Bi_mag(self) -> ndarray:
        return array([ abs(B) for B in self._data['Bi'] ])  
       
    def __str__ (self) -> str:
        problem_head = []
        problem_head.append( 'Campo magnetico\n'+60*'*'+'\n' )
        problem_head.append( 'Corrientes(s):\n' )
        currents = self._data['currents']
        problem_head += [f'I{ i+1 } = { I.I }A, posicionada en ({I.position.real},{I.position.imag}) m\n' 
                 for i,I in enumerate(currents)]
        problem_head.append( f'Punto en cuestión:\nP: ({ self._data["P"][0] },{ self._data["P"][1] }) m\n' )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Campo magnetico\n'+60*'*'+'\n'
        head = ''.join( problem_head ) + answer_head
        
        Bi_string = ''.join ( [ f'B{i+1} = {self.Bi[i]*1e6 } uT\n\n' for i in range( len(self.Bi) ) ] )
        
        B_strings = []
        B_strings.append( f'B = { self.B*1e6 } uT\n' )
        B_strings.append( f'|B| = { self.B_mag*1e6 } uT\n' )
        B_strings.append( 60*'*'+'\n\n' )
        return super().__str__( head,Bi_string  + ''.join(B_strings) ) 

class MagneticForceAnswer(problemAnswer):
    def __init__(self,**kargs ):
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
        problem_head.append( 'Fuerza de magnetica\n'+60*'*'+'\n' )
        problem_head.append( 'Corriente pasiva:\n' )
        problem_head = ''.join( problem_head )
        Pid: int = self._data["passive_I"][0]
        i: electricCurrent = self._data["passive_I"][1]
        I_str = f'I{ Pid } = { i.I }A, posicionada en ({i.position.real},{i.position.imag}) m\n\n' 
        active_I: dict[int,electricCurrent] = self._data["acting_currents"]
        active_I_str = ['Corriente(s) activa(s):\n']
        active_I_str += [f'I{id} = { Ia.I }A, posicionada en ({Ia.position.real},{Ia.position.imag}) m\n' 
                 for id,Ia in active_I.items()]
        active_I_str = ''.join( active_I_str )
        answer_head  = 60*'*'+'\nRespuesta al Problema de Fuerza Magnética\n'+60*'*'+'\n'
        head = problem_head + I_str + active_I_str + answer_head
        
        Fi_string = ''.join ( [ f'F{i+1} = {self.Fi[i]*1e3 } mN/m\n\n' for i in range( len(self.Fi) ) ] )
        
        F_strings = []
        F_strings.append( f'F = { self.F*1e3 } mN/m\n' )
        F_strings.append( f'|F| = { self.F_magnitud*1e3 } mN/m\n' )
        F_strings.append( 60*'*'+'\n\n' )
        return super().__str__( head,Fi_string +''.join( F_strings ) )
