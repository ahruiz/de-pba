palabra = input("ingresa una palabra al azar: ")
palabra = palabra.upper()
letra1 = ""
letra2 = ""
letra3 = ""
letra4 = ""
letraEnc= "" 

for letra in palabra:
        if  letra == "H" or letra == "O" or letra == "L" or letra == "A":
            match letra:
                case "H":
                    letra1 = letra
                case "O":
                    letra2 = letra
                case "L":
                    letra3 = letra
                case "A":
                    letra4 = letra

            letraEnc = letra1 + letra2 + letra3 + letra4

if  letra1 != "" and letra2 != "" and letra3 != "" and letra4 != "":
    print("-" * 60)
    print(f"de la palabra {palabra} se encontro la palabra: {letraEnc}")
    print("-" * 60)
else:
    print("-" * 60)
    print(f"no se encontro la palabra HOLA en la cadena {palabra}")
    print("-" * 60)

     