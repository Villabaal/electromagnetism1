# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

###To do a GUI
from numpy.random import randint
from matplotlib import pyplot as plt
from electric_mass.electric_currents import electricCurrent
from Questions.magneticQuestions import currentSystem


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




from matplotlib import pyplot as plt
from electric_mass.electric_charges import electricCharge
from Questions.electrostaticQuestions import chargeSystem
#carga del electron
e = -1.602177e-19

##Definicion de las cargas electricas y sus posiciones
charges = []
charges.append( electricCharge(8e13*e, (-1, -1)) )
charges.append( electricCharge(5.3e13*e, (3, 3)) )
charges.append( electricCharge(-1.4e13*e, (2, -0.5)) )
charges.append( electricCharge(-4.2e13*e, (-1, 2.5)) )

charges_ = charges.copy()
charges_.pop( randint( 0,len(charges_) ) )
# Define el sistema en el plano bidimensional
Space1 = chargeSystem( charges_ )
# Define el sistema en el plano bidimensional
Space2 = chargeSystem( charges )


## punto en cuestión para compo electrico
P = (2,0.5)

##Preguntas de test para Campo electrico y fuerza de coulomb
Answer1 = Space1.ElectricFieldQuestion(P,R=5)
Answer1.fig.savefig( 'P1 Campo Eléctrico.jpg',dpi = 1080 )
plt.show()
print( Answer1 ) 
file1 = open('P1 Campo Eléctrico.txt','w')
file1.write( Answer1.__str__() )
file1.close()

Answer2 = Space2.CoulombForceQuestion( charges[ randint( 0,len(charges)) ].id ,R=5)
Answer2.fig.savefig( 'P2 Fuerza de Coulomb.jpg',dpi = 1080 )
plt.show()
print( Answer2 ) 
file2 = open('P2 Fuerza de Coulomb.txt','w')
file2.write( Answer2.__str__() )
file2.close()