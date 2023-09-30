from utils import tuple2cmplx,Error

class _electricMass:    
    """Obejto de Carga Eléctrica, crea un campo eléctrico y sufre de repulsión o atracción.\n
            toma:
                - q o I : carga electrica o corriente electrica
                - p : indexable de tamaño 2
    """                
    def __init__(self,mass,p):
        if mass == 0: raise TypeError( "no se admiten cargas neutras" )
        if not hasattr( p ,'__getitem__'): raise TypeError( "p no es subscriptable" )
        if not ( len(p) == 2 ): raise TypeError( "len(p) no es 2" )
        self._mass,self.position = mass,tuple2cmplx( p )
        
    def _calculate_r(self,p):
        check_idx = 2*isinstance(p, tuple) + isinstance(p, complex) - 1
        return (  lambda : p - self.position, lambda : tuple2cmplx( p ) - self.position, 
               Error )[check_idx]()