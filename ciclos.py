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


# 5. Menor valor
def n_menor(n_numeros):
    menor = 999999999999999999
    for i in range(0, n_numeros):
        numero = int(input('Digite un numero: '))
        if (numero == 1):
            menor = numero
        else:
            if (numero < menor):
                menor = numero
    print('\nEl numero menor es --> ', menor)


n_menor(5)


# 6. Club en contra de la obesidad
def club(personas):
    for i in range(0, 5):
        acum_peso = 0
        promedio_peso = 0
        diferencia = 0
        ultimo = float(input(f'Ultimo peso de la persona {i+1}: --> '))
        for x in range(0, 10):
            peso = float(input(f'Digite el peso de la bascula {x+1}: --> '))
            acum_peso = acum_peso + peso
        promedio_peso = acum_peso / 10
        diferencia = promedio_peso - ultimo
        if (diferencia > 0):
            print(f'La persona {i+1} subio de peso', diferencia, 'kilos')
        else:
            print(f'La persona {i+1} bajo de peso', diferencia, 'kilos')


club(5)


# 7. Compra en un Supermercado
def supermercado():
    total = 0
    seguir = 'no'
    while (seguir == 'no' or seguir == 'NO'):
        nombre = input('Digite el nombre del articulo: ')
        cantidad = int(input(f'Digite la cantidad de {nombre} a comprar: '))
        precio = float(input(f'Digite el precio del articulo {nombre}: $'))
        total = total + (precio * cantidad)
        seguir = input('Desea finalizar su compra? --> ')
    print('pago total de la compra --> $', total)


supermercado()


# 8. Descuentos en un Teatro
def teatro(n_clientes):
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    categoria4 = 0
    categoria5 = 0
    precio = float(input('Digite el precio de los asientos --> $'))
    for i in range(0, n_clientes):
        edad_c = int(input(f'Digite la edad del cliente {i+1} --> '))
        if (edad_c >= 5 and edad_c <= 14):
            descuento_t = precio * 0.35
            categoria1 = categoria1 + descuento_t
        elif (edad_c >= 15 and edad_c <= 19):
            descuento_t = precio * 0.25
            categoria2 = categoria2 + descuento_t
        elif (edad_c >= 20 and edad_c <= 45):
            descuento_t = precio * 0.1
            categoria3 = categoria3 + descuento_t
        elif (edad_c >= 46 and edad_c <= 65):
            descuento_t = precio * 0.25
            categoria4 = categoria4 + descuento_t
        elif (edad_c >= 66):
            descuento_t = precio * 0.35
            categoria5 = categoria5 + descuento_t
    print('\nCantidad perdida en la categoria 1: $', categoria1)
    print('Cantidad perdida en la categoria 2: $', categoria2)
    print('Cantidad perdida en la categoria 3: $', categoria3)
    print('Cantidad perdida en la categoria 4: $', categoria4)
    print('Cantidad perdida en la categoria 5: $', categoria5)


teatro(20)


# 9. Comisiones a los vendedores de Kia Autos
def kia(n_empleados):
    for i in range(0, n_empleados):
        valor = float(input(f'Digite el valor vendido del empleado {i+1}: $'))
        if (valor <= 20000000):
            comision = valor * 0.1
            print('Su comision es de: ', comision)
        elif (valor > 20000000 and valor < 40000000):
            comision = valor * 0.15
            print('Su comision es de: ', comision)
        elif (valor >= 40000000 and valor < 80000000):
            comision = valor * 0.2
            print('Su comision es de: ', comision)
        elif (valor >= 80000000 and valor < 160000000):
            comision = valor * 0.25
            print('Su comision es de: ', comision)
        else:
            comision = valor * 0.3
            print('Su comision es de: ', comision)


kia(100)
