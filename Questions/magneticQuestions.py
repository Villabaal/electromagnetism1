
from matplotlib.patches import Circle

from electric_mass.electric_currents import electricCurrent
from utils import cmplx2tuple,isReal,tuple2cmplx
from Questions.space import Space
from Answers.magneticAnswers import MagneticFieldAnswer,MagneticForceAnswer



# clase usada para graficar los problemas de fuerza de coulomb y campo eléctrico
class currentSystem(Space):
    """Spacio bidimencional de cargas eléctricas estáticas.\n
            toma:
                - Is : iterable de electricCurrent (amperes)
    """                    
    def __init__(self, Is):
        Space.__init__(self, Is,electricCurrent)
        
    @Space._plot_field_
    def _MagneticField_(self, fig, splot ):
        for current in self._m.values():
            splot.add_artist(Circle(cmplx2tuple(current.position), 0.1, color = 'gray' ))
            splot.plot( *cmplx2tuple(current.position),marker=current.marker,color='red' )
        return fig,splot  
    
    #Coloca un punto sobre la grafica de campo electrico para generar un problema (ya solucionado)
    def MagneticFieldQuestion(self, P, n = 128, R = 1 ):
        """Coloca un punto sobre la grafica de campo electrico para generar un problema (ya solucionado).\n
                toma:
                    - P : indexable de tamaño 2
                    - n : numero de muestras de campo Eléctrico (para la gráfica)
                    - R : radio de pantalla mas R\n
                regresa:
                    - Obejto EletricFieldAnswer (con la gráfica y datos principales)
                    
        """            
        if not hasattr( P ,'__getitem__'): raise TypeError( "P no es subscriptable" )
        if not ( len(P) == 2 ): raise ValueError( "len(P) no es 2" )
        if any( [ not isReal( component ) for component in P ] ): 
            raise TypeError( "componentes deben ser numeros Reales" )
        self._check_window(n,R)     
        fig, splot = self._MagneticField_( n, R, tuple2cmplx( P ) )
        r = [ tuple2cmplx( P ) - current.position for current in self._m.values() ]
        Bi =  [ current.B(P)  for current in self._m.values()]
        Bp = sum( Bi )
        for i,current in enumerate(self._m.values()):
            splot.arrow( *cmplx2tuple(current.position) , *cmplx2tuple(r[i]), 
                head_width=0.1, head_length=0.25,
                color='purple',linestyle='--',length_includes_head = True)
            splot.arrow( *P , *cmplx2tuple( current.sign*1j*r[i]/abs( r[i] ) ) , 
                head_width=0.15, head_length=0.3,
                color='darkblue',length_includes_head = True)
        if abs(Bp) != 0: 
            splot.arrow( *P , *cmplx2tuple( Bp/abs( Bp ) ) , 
                head_width=0.15, head_length=0.3,
                color='darkred',length_includes_head = True)            
        splot.add_artist( Circle( P, 0.05, color = 'k') )
        return MagneticFieldAnswer( currents = self._m.values(), P = P ,
                                  fig = fig, splot = splot, Bi = Bi , B = Bp , r = r )
    
    #Elige una de las cargas por id (int) 1,2,3... y calcula la fuerza resultante
    def MagneticForceQuestion(self, current_id, n = 128, R = 1): 
        """Elige una de las cargas por charge_id (int) 1,2,3... 
            y calcula la fuerza resultante que incide en ella \n
                Toma:
                    - charge_id : el id de la carga en cuestión
                    - n : numero de muestras de campo Eléctrico (para la gráfica)
                    - R : radio de pantalla mas R\n 
                    regresa:
                        - Obejto CoulombForceAnswer (con la gráfica y datos principales)
        """
        if not isinstance(current_id,int) : raise TypeError( "current_id must be int" )        
        self._check_window(n,R)
        fig, splot = self._MagneticField_( n, R )
        I = self._m[current_id]
        acting_currents = [ current for m_id,current in self._m.items() if m_id != current_id ]
        r = [ current.position - I.position for current in acting_currents ]
        F = sum( [ I.F(current) for current in acting_currents] )
        for i,current in enumerate( acting_currents ):
            splot.arrow( *cmplx2tuple(I.position) ,
                *cmplx2tuple( r[i] ), head_width=0.1, head_length=0.25,
                color='purple',linestyle='--',length_includes_head = True)
            action = I.sign*current.sign
            if action > 0: # se atraen el punto final sera la carga en cuestion
                splot.arrow( *cmplx2tuple( I.position - r[i]/abs( r[i] ) ) ,
                    *cmplx2tuple( r[i]/abs( r[i] ) ) , 
                    head_width=0.15, head_length=0.3, color='#0000FF',length_includes_head = True)
                
            elif action < 0: # se repelen el punto inicial sera la carga en cuestion
                splot.arrow( *cmplx2tuple( I.position ) ,
                    *cmplx2tuple( -r[i]/abs( r[i] ) ) , 
                    head_width=0.15, head_length=0.3, color='#FF0000',length_includes_head = True)
                
        if  (len(acting_currents) > 1) and ( abs( F ) != 0 ) :
            splot.arrow( *cmplx2tuple( I.position ) ,
                    *cmplx2tuple( F/abs( F ) ) , 
                    head_width=0.15, head_length=0.3, color='k',length_includes_head = True)            
        return MagneticForceAnswer( passive_I = I, acting_currents=acting_currents 
                                  ,fig = fig, splot = splot , F = F , r = r )
        