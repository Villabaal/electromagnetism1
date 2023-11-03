# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from random import randrange
from utils import randomPoint
from random import uniform
from matplotlib import pyplot as plt
from electric_mass.electric_currents import electricCurrent
from Questions.magneticQuestions import currentSystem



### To do interface grafica
for i in range(1):
##Definicion de las cargas electricas y sus posiciones
    currents = [ electricCurrent(round( uniform(-200,200), 3), randomPoint() ) for _ in range(2)]
    Space = currentSystem( currents )
    ## punto en cuestión para compo electrico
    P = randomPoint()
    ##Preguntas de test para Campo electrico y fuerza de coulomb
    Answer = Space.MagneticFieldQuestion(P,R=2)
    Answer.fig.savefig( f'P{ Answer.id } Campo Manetico.jpg',dpi = 1080 )
    plt.show()
    print( Answer ) 
    with open(f'P{ Answer.id } Campo Manetico.txt','w') as file:
        file.write( Answer.__str__() )

# Answer2 = Space2.MagneticForceQuestion(  currents[ randrange( len(currents) ) ].id  ,R=4.5)
# Answer2.fig.savefig( f'P{ Answer2.id } Fuerza Manetica.jpg',dpi = 1080 )
# plt.show()
# print( Answer2 ) 
# with open(f'P{ Answer2.id } Fuerza Manetica.txt','w') as file:
#     file.write( Answer2.__str__() )



# from electric_mass.electric_charges import electricCharge
# from Questions.electrostaticQuestions import chargeSystem
# #carga del electron
# e = -1.602177e-19

# ##Definicion de las cargas electricas y sus posiciones
# charges = []
# charges.append( electricCharge(6e13*e, (-1, -1.5)) )
# charges.append( electricCharge(-2.4e13*e, (2, -1)) )
# charges.append( electricCharge(5.2e13*e, (1, 2.5)) )

# charges_ = charges.copy()
# charges_.pop( randrange( len(charges) ) )
# # Define el sistema en el plano bidimensional
# Space3 = chargeSystem( charges_ )
# # Define el sistema en el plano bidimensional
# Space4 = chargeSystem( charges )


# ## punto en cuestión para compo electrico
# P = (-3,-2)

# ##Preguntas de test para Campo electrico y fuerza de coulomb
# Answer1 = Space3.ElectricFieldQuestion(P,R=6)
# Answer1.fig.savefig( f'P{ Answer1.id } Campo Eléctrico.jpg',dpi = 1080 )
# plt.show()
# plt.close()
# print( Answer1 ) 
# with open(f'P{ Answer1.id } Campo Eléctrico.txt','w') as file:
#     file.write( Answer1.__str__() )


# Answer2 = Space4.CoulombForceQuestion( charges[ randrange( len(charges) ) ].id ,R=5)
# Answer2.fig.savefig( f'P{ Answer2.id } Fuerza de Coulomb.jpg',dpi = 1080 )
# plt.show()
# plt.close()
# print( Answer2 ) 
# with open(f'P{ Answer2.id } Campo Eléctrico.txt','w') as file:
#     file.write( Answer2.__str__() )