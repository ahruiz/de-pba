from colorama import Fore, Style, Back


tabla = input("Teclea la tabla de multiplicar que quieres generar: ")
multiplo = input("Indica hasta que multiplo quieres la tabla: ")
i = multiplo
cont = 1
result = 0

if not tabla.isdigit() or not multiplo.isdigit():
    print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
    print("Debes introducir  numeros enteros y no otro tipo de caracter...")
    print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
    exit()
    
i = int(i)
multiplo = int(multiplo)
tabla = int(tabla)
result = int(result)

if  i <= multiplo:
    while cont <= multiplo:
        result = tabla * cont
        print(f"{Fore.YELLOW}  {tabla} * {cont} = {result}  {Fore.WHITE}")
        cont += 1
        i += 1
    
