import random

# generamos un num aleatorio entre 1 y 10 y se guarda en 

print("***proceso generador de numero escondido aleatorio entre 1 y 10***")
hidenNum=random.randint(1, 10)

cont = 0

while True:
    numero = input("escribe el numero que piensas que se generó: ")

    if  not numero.isdigit():
        print("-" * 60)
        print("debes ingresar un numero, no caracteres diferentes")
        print("-" * 60)
        continue 
    numero = int(numero)
    if numero < 1 or numero > 10 :
        print("-" * 60)
        print("Debes teclear numeros del 1 al 10")
        print("-" * 60)
        continue
    cont += 1
    if numero < hidenNum:
        print("-" * 60)
        print("Te quedaste corto!!!...ingresa un numero mayor")
        print("-" * 60)
    elif numero > hidenNum:
        print("-" * 60)
        print("Te pasaste!!!!....ingresa un numero mas chico")
        print("-" * 60)
    else:
        print("-" * 60)
        print(f"FELICIDADES!!!!! adivinaste el numero en {cont} intentos")
        print("-" * 60)
        break
