from math import *

#Autores: Sebastián Israel González Muñiz A01570959, Sofía Ríos Guajardo A01284653 & Santiago Makoszay Castañón
#Este programa determina el perímetro y área de figuras geométricas


#Saludar y preguntar nombre
print ("¡Hola, lindo día!")
print ("¿Cómo te llamas?")
nombre = input()

#Responder con cortesía
print ("Buenas tardes " + nombre)
print ("Bienvenido a tu calculadora de figuras geométricas 3000")

while True: 
#Pide figura geométrica
    print ("¿De qué figura geométrica te gustaría calcular sus medidas?")
    print ("1. Círculo")
    print ("2. Cuadrado")
    print ("3. Rectágulo")
    print ("4. Triángulo")
    figura = int(input())

    #Pide medidas y calcula medida de las figuras geométricas
    if figura == 1 :
        radio = float(input("Por favor proporciona la magnitud del radio del círculo: "))
        perimetro = (radio*2) * pi
        area = pi * (radio**2)
        print ("El área del círculo es " + str(area) + " y el perímetro es " + str(perimetro))
    elif figura == 2:
        lado = float(input("Por favor proporciona la magnitud del lado del cuadrado: "))
        perimetro = lado*4
        area = lado**2
        print ("El área del cuadrado es " + str(area) + " y el perímetro es " + str(perimetro))
    elif figura == 3:
        lado_mayor = float(input("Por favor proporciona la magnitud del lado mayor: "))
        lado_menor = float(input("Por favor proporciona la magnitud del lado menor: "))
        perimetro = lado_mayor*2 + lado_menor*2
        area = lado_mayor * lado_menor
        print ("El área del rectángulo es " + str(area) + " y el perímetro es " + str(perimetro))
    else:
        base = float(input("Por favor proporciona la magnitud de la base: "))
        altura = float(input("Por favor proporciona la magnitud de la altura: "))
        lado_dos = float(input("Por favor proporciona la magnitud del lado 2 (cualquiera de los otros dos lados que no sean la base): "))
        lado_tres = float(input("Por favor proporciona la magnitud del lado 3 (el otro lado que no sea la base ni el lado 2): "))
        perimetro = base + lado_dos + lado_tres
        area = (base * altura)/2
        print ("El área del rectángulo es " + str(area) + " y el perímetro es " + str(perimetro))
    
    print ("¿Quieres calcular las medidas de alguna otra figura?")
    print ("1. Sí")
    print ("2. No")
    decision = int(input())
    if decision == 2:
        break
    
#Agradece y se despide     
print ("¡listo " + nombre + "!, gracias por usar tu calculadora de figuras geométricas 3000 ;)")
    