from collections import Counter
from colorama import Fore
import re

print(Fore.YELLOW +  "-" * 60 + Fore.WHITE) #linea de separacion en pantalla
print(f"{Fore.GREEN} Codigo para analizar texto desde el teclado o archivo....{Fore.WHITE}") # explicacion
print(Fore.YELLOW +  "-" * 60 + Fore.WHITE)

metodo = input("introduce (T) para Texto o (A) para Archivo: ") # pedimos capturar el metodo
metodo = metodo.upper() #convertimos a mayusculas

if metodo == "T" or metodo == "A":
    if metodo == "T":
        texto = input("Ingresa el TEXTO a analizar: ") # pedimos al usr capturar el texto

        texto_limpio = re.sub(r'[^a-z\s]', '', texto) #elimina caracteres distintos a letras y se remplazan con espacios en la cadena "texto"

        texto = texto_limpio          # queda el texto sin espacios

        palabras = texto.split()      # se genera la lista PALABRAS con cada una de las palabras del txt
        numPalabras = len(palabras)   # se verifica la longitud de la lista

        longitud_maxima = max(len(palabra) for palabra in palabras)    #se determina la long de cada palabra y guarda la longitud mas larga
            # palMasL = max(palabras, key = len)....este cmd elimina los dos cms (ant y post) y ya saca la palabra mas larga
            # lonPalMasL = len(palMasL) sacamos la long de la palabra mas larga
        palabras_mas_largas = [palabra for palabra in palabras if len(palabra) == longitud_maxima]  # se elige la mas larga

        dict = {}     # se genera un diccionario vacio

        for letra in texto:
            if letra in dict:
                dict[letra] += 1 # se incrementa el numero de la letra (ya existe)
            else:
                dict[letra] = 1  # se inserta e iguala a uno si no existe(nueva)

        contPal = Counter(palabras)     # contamos las palabras de la lista palabras
        contLet = Counter(dict)         # contamos las letras del dictionario
        palMasC = contPal.most_common(2) #  se determinan las dos palabras mas comunes
        letMasC = contLet.most_common(2) # se determina cual letra es la mas comun

        print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
        print(f"El texto contiene las palabras: {Fore.YELLOW} {palabras} {Fore.WHITE} y son {Fore.YELLOW} {numPalabras} {Fore.WHITE} palabras")
        print(f"La palabra mas comun es: {Fore.YELLOW} {palMasC} {Fore.WHITE} y la letra mas comun es: {Fore.YELLOW} {letMasC} {Fore.WHITE}")
        print(f"La palabra mas largas es: {Fore.YELLOW} {palabras_mas_largas} {Fore.WHITE} con una logitud de {Fore.YELLOW} {longitud_maxima} {Fore.WHITE} letras")
        print(Fore.YELLOW +  "-" * 120 + Fore.WHITE)
    else:
        archivo = input("introduce el nombre del archivo a analizar: ")
        try:
            arch = open(archivo, 'r')   # abrimos el archivo
            palabras = arch.readline()   # se lee arch linea por linea
            arch.close()                # cerramos el arch
            
            numpal = palabras.split()    # creamos la lista numpal con las palabras del archivo
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

dict.clear            #reiniciamos dictionario y numPalabras
numPalabras = 0
