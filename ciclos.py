#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:31:26 2021

@author: ivandavid
"""


# 1. Transito de Barranquilla
def transito_baq(n_autos, digito):
    n_autos = int(input('Digite el número de autos que ingresaron: '))
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    for x in range(n_autos):
        digito = int(input(f'Último digito del auto {x+1}: --> '))
        if (digito == 1 or digito == 2):
            cont1 = cont1 + 1
            print('¡Entro con calcomanía amarilla!')
        elif (digito == 3 or digito == 4):
            cont2 = cont2 + 1
            print('¡Entro con calcomanía rosa!')
        elif (digito == 5 or digito == 6):
            cont3 = cont3 + 1
            print('¡Entro con calcomanía roja!')
        elif (digito == 7 or digito == 8):
            cont4 = cont4 + 1
            print('¡Entro con calcomanía verde!')
        elif (digito == 9 or digito == 0):
            cont5 = cont5 + 1
            print('¡Entro con calcomanía azul!')

    print('\nCantidad de autos que entraron con calcomania amarilla: ', cont1)
    print('Cantidad de autos que entraron con calcomania rosa: ', cont2)
    print('Cantidad de autos que entraron con calcomania roja: ', cont3)
    print('Cantidad de autos que entraron con calcomania verde: ', cont4)
    print('Cantidad de autos que entraron con calcomania azul: ', cont5)


transito_baq(0, 0)
