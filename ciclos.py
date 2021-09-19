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


# 2. Porcentaje de animales por edades
def zoo(animal):
    acum1 = 0
    acum2 = 0
    acum3 = 0
    acum4 = 0
    acum5 = 0
    acum6 = 0
    acum7 = 0
    acum8 = 0
    acum9 = 0
    if (animal == 'elefantes'):
        print('\nAnimal a estudiar --> Elefantes')
        for i in range(0, 20):
            edad = int(input(f'Animal {i+1} edad: '))
            if (edad <= 1):
                acum1 = acum1 + 1
            elif (edad > 1 and edad < 3):
                acum2 = acum2 + 1
            elif (edad >= 3):
                acum3 = acum3 + 1
            cat1 = (acum1*100) / 20
            cat2 = (acum2*100) / 20
            cat3 = (acum3*100) / 20
        print(f'\nPorcentaje de  edad  [0 a 1] en elefantes -->  {cat1}%')
        print(f'Porcentaje de  edad  [2 años ] en elefantes -->  {cat2}%')
        print(f'Porcentaje de  edad  [3 o mas años] en elefantes -->  {cat3}%')

    elif (animal == 'jirafas'):
        print('\nAnimal a estudiar --> Jirafas')
        for i in range(0, 15):
            edad = int(input(f'Animal {i+1} edad: '))
            if (edad <= 1):
                acum4 = acum4 + 1
            elif (edad > 1 and edad < 3):
                acum5 = acum5 + 1
            elif (edad >= 3):
                acum6 = acum6 + 1
            cat1 = (acum4*100) / 15
            cat2 = (acum5*100) / 15
            cat3 = (acum6*100) / 15
        print(f'\nPorcentaje de  edad  [0 a 1] en jirafas -->  {cat1}%')
        print(f'Porcentaje de  edad  [2 años ] en jirafas -->  {cat2}%')
        print(f'Porcentaje de  edad  [3 o mas años] en jirafas -->  {cat3}%')

    elif (animal == 'chimpances'):
        print('\nAnimal a estudiar --> Chimpances')
        for i in range(0, 40):
            edad = int(input(f'Animal {i+1} edad: '))
            if (edad <= 1):
                acum7 = acum7 + 1
            elif (edad > 1 and edad < 3):
                acum8 = acum8 + 1
            elif (edad >= 3):
                acum9 = acum9 + 1
            cat1 = (acum7*100) / 40
            cat2 = (acum8*100) / 40
            cat3 = (acum9*100) / 40
        print(f'\nPorcentaje de edad  [0 a 1] en chimpances -->  {cat1}%')
        print(f'Porcentaje de edad  [2 años ] en chimpances -->  {cat2}%')
        print(f'Porcentaje de edad  [3 o mas años] en chimpances -->  {cat3}%')


zoo('jirafas')


# 3. Salario semanal de los obreros en una empresa
def obreros(n_obreros):
    for i in range(n_obreros):
        hora = int(input(f'Digite las horas de trabajo del obrero {i+1} --> '))
        if (hora <= 40):
            pago_total = 20 * hora
            print(f'\nsalario del obrero {i+1}: ${pago_total}')
        elif (hora > 40):
            hora_extra = int(input('Digite las horas extras: '))
            extras = (hora - 40)
            pago_primeras = (20 * 40)
            pago_extra = ((hora_extra + extras) * 25)
            pago_total_extra = pago_extra + pago_primeras
            print(f'\nsalario con horas extras: ${pago_total_extra}')


obreros(4)


# 4. Promedio de edades de hombres y mujeres
def p_edades(n_alumnos):
    acumh = 0
    acumm = 0
    edadh = 0
    edadm = 0
    for i in range(0, n_alumnos):
        genero = input(f'Digite el genero del estudiante {i+1}: --> ')
        edades = int(input(f'Digite la edad del estudiante {i+1}: --> '))
        if (genero == 'hombre'):
            acumh = acumh + 1
            edadh = edadh + edades
            promedioh = edadh / acumh
        elif (genero == 'mujer'):
            acumm = acumm + 1
            edadm = edadm + edades
            promediom = edadm / acumm
    promedio_grupo = (edadh + edadm) / n_alumnos
    print('\nPromedio de edades Hombres: ', promedioh)
    print('Promedio de edades Mujeres: ', promediom)
    print('Promedio de edades de todo el grupo: ', promedio_grupo)


p_edades(5)
