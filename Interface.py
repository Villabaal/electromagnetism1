# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy.random import randint
from matplotlib import pyplot as plt
from electric_mass.electric_currents import electricCurrent
from Questions.magneticQuestions import currentSystem

### To do interface grafica

##Definicion de las cargas electricas y sus posiciones
currents = []
currents.append( electricCurrent(40, (-1, -1)) )
currents.append( electricCurrent(40, (1, 1)) )
currents.append( electricCurrent(-50, (2, -0.5)) )


currents_ = currents.copy()
currents_.pop( 2 )#pop( randint( 0,len(currents) ) )
# Define el sistema en el plano bidimensional
Space1 = currentSystem( currents_ )
# Define el sistema en el plano bidimensional
Space2 = currentSystem( currents )


## punto en cuestión para compo electrico
P = (2,0.5)

##Preguntas de test para Campo electrico y fuerza de coulomb
Answer1 = Space1.MagneticFieldQuestion(P,R=4.5)
Answer1.fig.savefig( 'P1 Campo Manetico.jpg',dpi = 1080 )
plt.show()
print( Answer1 ) 
file1 = open('P1 Campo Manetico.txt','w')
file1.write( Answer1.__str__() )
file1.close()

Answer2 = Space2.MagneticForceQuestion(  currents[ randint( 0,len(currents)) ].id  ,R=4.5)
Answer2.fig.savefig( 'P2 Fuerza Manetica.jpg',dpi = 1080 )
plt.show()
print( Answer2 ) 
file2 = open('P2 Fuerza Manetica.txt','w')
file2.write( Answer2.__str__() )
file2.close()



from electric_mass.electric_charges import electricCharge
from Questions.electrostaticQuestions import chargeSystem
#carga del electron
e = -1.602177e-19

##Definicion de las cargas electricas y sus posiciones
charges = []
charges.append( electricCharge(6e13*e, (-1, -1.5)) )
charges.append( electricCharge(-2.4e13*e, (2, -1)) )
charges.append( electricCharge(5.2e13*e, (1, 2.5)) )

charges_ = charges.copy()
charges_.pop( randint( 0,len(charges_)-1 ) )
# Define el sistema en el plano bidimensional
Space3 = chargeSystem( charges_ )
# Define el sistema en el plano bidimensional
Space4 = chargeSystem( charges )


## punto en cuestión para compo electrico
P = (-3,-2)

##Preguntas de test para Campo electrico y fuerza de coulomb
Answer1 = Space3.ElectricFieldQuestion(P,R=6)
Answer1.fig.savefig( f'P{ Answer1.id } Campo Eléctrico.jpg',dpi = 1080 )
plt.show()
plt.close()
print( Answer1 ) 
with open(f'P{ Answer1.id } Campo Eléctrico.txt','w') as file:
    file.write( Answer1.__str__() )


Answer2 = Space4.CoulombForceQuestion( charges[ randint( 0,len(charges)) ].id ,R=5)
Answer2.fig.savefig( f'P{ Answer2.id } Fuerza de Coulomb.jpg',dpi = 1080 )
plt.show()
plt.close()
print( Answer2 ) 
with open(f'P{ Answer2.id } Campo Eléctrico.txt','w') as file:
    file.write( Answer2.__str__() )