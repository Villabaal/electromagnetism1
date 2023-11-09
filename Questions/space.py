from matplotlib.pyplot import ioff
from collections.abc import Iterable
from numpy import array,linspace,meshgrid,sort,log10,pi
from cmath import rect
import matplotlib.pyplot as plt
from utils import isReal
import functools


class Space:
    """Spacio bidimencional de cargas eléctricas estáticas.\n
            toma:
                - masses : iterable de electricCharge o electricCurrent
    """                    
    def __init__(self, masses, Type):
        self._type = Type
        self.masses = masses
        ioff()
        
    @property
    def masses(self): return self._m
    
    @masses.setter
    def masses(self, masses ): 
        if not isinstance(masses,Iterable): raise TypeError( "Masas no es iterables" )
        if any( [ not isinstance(mass,self._type) for mass in masses ] ):
            raise TypeError( "uno o mas elemenos invalidos" )
        self._m = { i+1:mass for i,mass in enumerate(masses) }
        
    def _check_window(self,n,R):
        if not isinstance(n,int) : raise TypeError( "n must be int" )
        if not isReal( R ) : raise TypeError( "R debe ser real" )
        if  ( R<=0 ): raise TypeError( "R debe ser positivo" ) 
    
    def _plot_field_( field ):
        @functools.wraps( field )
        def wrapper_decorator(self, n, offset, P = None):
            # numero del centro de la grafica (promedio de los vectores de pocision)
            masses_positions = [ mass.position for mass in self.masses.values() ]
            if P is not None:
                masses_positions.append(P)
            massCenter = sum( masses_positions )/len(masses_positions)
            R = max( [ abs( position - massCenter ) for position in masses_positions ] ) + offset
            # encuadre de la grafica
            offsets = array( [ rect( R, (i*4+1)*pi/4 ) for i in range(2)] )                
            limits = offsets + massCenter
            x = linspace( *sort(limits.real) , n )
            y = linspace( *sort(limits.imag) , n )
            X, Y = meshgrid(x,y)
            Grid = (X,Y)
            Field = sum( [ mass._field(Grid)  for mass in self.masses.values()] )
            fig, splot = plt.subplots()
            color = log10( abs(Field) )
            splot.streamplot(x,y,Field.real, Field.imag, color=color, 
                             linewidth=0.5, cmap=plt.cm.inferno, density = 2,
                             arrowstyle='->', arrowsize=1)
            splot.set_xlabel( "x (meters)" )
            splot.set_ylabel( "y (meters)" )
            splot.axvline(0,color='k')
            splot.axhline(0,color='k')
            return field(self, fig, splot )
            # Do something after
        return wrapper_decorator
    

