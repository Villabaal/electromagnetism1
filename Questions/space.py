from matplotlib.pyplot import ioff
from matplotlib.figure import Figure
from collections.abc import Iterable
from numpy import linspace,meshgrid,log10
from matplotlib.pyplot import cm
import functools
from electric_mass import electricCurrent,electricCharge


class Space:
    """Espacio bidimencional de cargas eléctricas estáticas.\n
            toma:
                - masses : iterable de electricCharge o electricCurrent
    """                    
    def __init__(self, masses, Type):
        self._type = Type
        self.masses = masses
        ioff()
        
    @property
    def masses(self) -> dict[int,electricCurrent|electricCharge]: return self._m
    
    @masses.setter
    def masses(self, masses: Iterable[electricCurrent|electricCharge] ) -> None: 
        if not isinstance(masses,Iterable): raise TypeError( "Masas no es iterables" )
        if any( [ not isinstance(mass,self._type) for mass in masses ] ):
            raise TypeError( "uno o mas elemenos invalidos" )
        self._m = { i+1:mass for i,mass in enumerate(masses) }
        
    def _check_window(self,n):
        if not isinstance(n,int) : raise TypeError( "n must be int" )
    
    def _plot_field_( field ):
        @functools.wraps( field )
        def wrapper_decorator(self,fig: Figure, n:int):
            field( self , fig )
            splot = fig.axes[0]            
            x_lim = splot.get_xlim()
            y_lim = splot.get_ylim()
            x = linspace( *x_lim, n )
            y = linspace( *y_lim, n )
            X, Y = meshgrid(x,y)
            Grid = (X,Y)
            Field = sum( [ mass._field(Grid)  for mass in self.masses.values()] )
            color = log10( abs(Field) )
            splot.streamplot(x,y,Field.real, Field.imag, color=color, 
                             linewidth=0.5, cmap= cm.inferno, density = 2,
                             arrowstyle='->', arrowsize=1)
            splot.set_xlim(x_lim)
            splot.set_ylim(y_lim)
            splot.set_xlabel( "x (meters)" )
            splot.set_ylabel( "y (meters)" )
            splot.axvline(0,color='k')
            splot.axhline(0,color='k')
        return wrapper_decorator
    

