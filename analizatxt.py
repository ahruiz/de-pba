from collections import Counter
from colorama import Fore
import re

print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
print(f"{Fore.GREEN} Codigo para analizar texto desde el teclado o archivo....{Fore.WHITE}")
print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)

metodo = input("introduce (T) para Texto o (A) para Archivo: ")
metodo = metodo.upper()

if metodo == "T" or metodo == "A":
    if metodo == "T":
        texto = input("Ingresa el TEXTO a analizar: ")

        texto_limpio = re.sub(r'[^a-z\s]', '', texto) #elimina caracteres distintos a letras y espacios

        texto = texto_limpio

        palabras = texto.split()
        numPalabras = len(palabras)

        longitud_maxima = max(len(palabra) for palabra in palabras) #se determina la long de cada palabra
        palabras_mas_largas = [palabra for palabra in palabras if len(palabra) == longitud_maxima]  # se elige la mas larga

        dict = {}
        for letra in texto:
            if letra in dict:
                dict[letra] += 1
            else:
                dict[letra] = 1

        contPal = Counter(palabras)
        contLet = Counter(dict)
        palMasC = contPal.most_common(2)
        letMasC = contLet.most_common(2)

        print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
        print(f"El texto contiene las palabras: {Fore.YELLOW} {palabras} {Fore.WHITE} y son {Fore.YELLOW} {numPalabras} {Fore.WHITE} palabras")
        print(f"La palabra mas comun es: {Fore.YELLOW} {palMasC} {Fore.WHITE} y la letra mas comun es: {Fore.YELLOW} {letMasC} {Fore.WHITE}")
        print(f"La palabra mas largas es: {Fore.YELLOW} {palabras_mas_largas} {Fore.WHITE} con una logitud de {Fore.YELLOW} {longitud_maxima} {Fore.WHITE} letras")
        print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
    else:
        archivo = input("introduce el nombre del archivo a analizar: ")
        try:
            arch = open(archivo, 'r')
            palabras = arch.readline()
            arch.close()
            
            numpal = palabras.split()
            texto_limpio = re.sub(r'[^a-z\s,^A-Z\s,^0-9\s]', '', palabras) #elimina caracteres distintos a letras (May, Min), Nums y espacios
            numpal = texto_limpio.split()
            numPalabras = len(numpal)
            
            longitud_maxima = max(len(palabra) for palabra in numpal) #se determina la long de cada palabra
            palabras_mas_largas = [palabra for palabra in numpal if len(palabra) == longitud_maxima]  # se elige la mas larga

            dict = {} 
            for letra in palabras:
                if letra in dict:
                    dict[letra] += 1
                else:
                    dict[letra] = 1

            contPal = Counter(numpal)
            contLet = Counter(dict)
            palMasC = contPal.most_common(2)
            letMasC = contLet.most_common(2)

            print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
            print(f"El Archivo contiene las palabras: {Fore.YELLOW} {numpal} {Fore.WHITE} y son {Fore.YELLOW} {numPalabras} {Fore.WHITE} palabras")
            print(f"La palabra mas comun es: {Fore.YELLOW} {palMasC} {Fore.WHITE} y la letra mas comun es: {Fore.YELLOW} {letMasC} {Fore.WHITE}")
            print(f"La palabra mas largas es: {Fore.YELLOW} {palabras_mas_largas} {Fore.WHITE} con una logitud de {Fore.YELLOW} {longitud_maxima} {Fore.WHITE} letras")
            print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
        except FileNotFoundError:
            print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
            print("El archivo no existe o se tecleo mal.....")
            print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
else:
    print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)
    print("Debe teclear (T) para texto o (A) para Archivo....")
    print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)

dict.clear
numPalabras = 0