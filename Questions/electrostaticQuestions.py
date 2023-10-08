
from matplotlib.patches import Circle

from electric_mass.electric_charges import electricCharge
from utils import cmplx2tuple,isReal,tuple2cmplx
from Questions.space import Space
from Answers.electrostaticAnswers import EletricFieldAnswer,CoulombForceAnswer



# clase usada para graficar los problemas de fuerza de coulomb y campo eléctrico
class chargeSystem(Space):
    """Spacio bidimencional de cargas eléctricas estáticas.\n
            toma:
                - Q : iterable de electricCharge (amperes)
    """                    
    def __init__(self, Q):
        Space.__init__(self, Q,electricCharge)
        
    #Genera una grafica de campo electrico y devuelve el objeto figura (grafica)
    def _ElectricField(self, n, R, P = None):
        fig,splot= Space._plot_field(self, n, R , P)
        for _,charge in self._m.items():
            splot.add_artist(Circle(cmplx2tuple(charge.position), 0.1, color = charge.color ))
        return fig,splot
    
    
    #Coloca un punto sobre la grafica de campo electrico para generar un problema (ya solucionado)
    def ElectricFieldQuestion(self, P, n = 128, R = 5 ):
        """Coloca un punto sobre la grafica de campo electrico para generar un problema (ya solucionado).\n
                toma:
                    - P : indexable de tamaño 2
                    - n : numero de muestras de campo Eléctrico (para la gráfica)
                    - R : 2R es el tamaño de pantalla de la gráfica\n
                regresa:
                    - Obejto EletricFieldAnswer (con la gráfica y datos principales)
                    
        """            
        if not hasattr( P ,'__getitem__'): raise TypeError( "P no es subscriptable" )
        if not ( len(P) == 2 ): raise TypeError( "len(P) no es 2" )
        if any( [ not isReal( component ) for component in P ] ): 
            raise TypeError( "componentes deben ser numeros Reales" )
        self._check_window(n,R)     
        fig, splot = self._ElectricField( n, R , tuple2cmplx( P ) )
        r = [ tuple2cmplx( P ) - charge.position for charge in self._m.values() ]
        Ep = sum( [ charge.E(P)  for charge in self._m.values()] )
        for i,charge in enumerate( self._m.values() ):
            splot.arrow( *cmplx2tuple(charge.position) , *cmplx2tuple(r[i]), head_width=0.1, head_length=0.25,
                color='purple',linestyle='--',length_includes_head = True)
            splot.arrow( *P , *cmplx2tuple( charge.sign*r[i]/abs( r[i] ) ) , head_width=0.15, head_length=0.3,
                color=charge.color,length_includes_head = True)
        if abs(Ep) != 0: splot.arrow( *P , *cmplx2tuple( Ep/abs( Ep ) ) , head_width=0.15, head_length=0.3,
            color='darkred',length_includes_head = True)            
        splot.add_artist( Circle( P, 0.05, color = 'k') )
        return EletricFieldAnswer( charges = self._m.values(), P = P ,
                                  fig = fig, splot = splot , E = Ep , r = r )
    
    #Elige una de las cargas por id (int) 1,2,3... y calcula la fuerza resultante
    def CoulombForceQuestion(self, charge_id, n = 128, R = 5): 
        """Elige una de las cargas por charge_id (int) 1,2,3... 
            y calcula la fuerza resultante que incide en ella \n
                Toma:
                    - charge_id : el id de la carga en cuestión
                    - n : numero de muestras de campo Eléctrico (para la gráfica)
                    - R : 2R es el tamaño de pantalla de la gráfica\n 
                    regresa:
                        - Obejto CoulombForceAnswer (con la gráfica y datos principales)
        """
        if not isinstance(charge_id,int) : raise TypeError( "charge_id must be int" )        
        self._check_window(n,R)
        fig, splot = self._ElectricField( n, R )
        q = self._m[charge_id]
        acting_charges = [ charge for m_id,charge in self._m.items() if m_id != charge_id ]
        r = [ q.position - charge.position for charge in acting_charges ]
        F = sum( [ q.F(charge) for charge in acting_charges] )
        for i,charge in enumerate( acting_charges ):
            splot.arrow( *cmplx2tuple(charge.position) ,
                *cmplx2tuple( r[i] ), head_width=0.1, head_length=0.25,
                color='purple',linestyle='--',length_includes_head = True)
            action = q.sign*charge.sign
            if action < 0: # se atraen el punto final sera la carga en cuestion
                splot.arrow( *cmplx2tuple( q.position + r[i]/abs( r[i] ) ) ,
                    *cmplx2tuple( action*r[i]/abs( r[i] ) ) , 
                    head_width=0.15, head_length=0.3, color='#0000FF',length_includes_head = True)
            elif action > 0: # se repelen el punto final sera la carga en cuestion
                splot.arrow( *cmplx2tuple( q.position ) ,
                    *cmplx2tuple( r[i]/abs( r[i] ) ) , 
                    head_width=0.15, head_length=0.3, color='#FF0000',length_includes_head = True)
        if  (len(acting_charges) > 1) and ( abs( F ) != 0 ) :
            splot.arrow( *cmplx2tuple( q.position ) ,
                    *cmplx2tuple( F/abs( F ) ) , 
                    head_width=0.15, head_length=0.3, color='k',length_includes_head = True)            
        return CoulombForceAnswer( passive_charge=q, acting_charges=acting_charges 
                                  ,fig = fig, splot = splot , F = F , r = r )
        