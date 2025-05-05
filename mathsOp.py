numa = 5
numb = 12

def opSuma():
    input("Escribe el primer num a sumar: ")
    input("Escribe el segundo numero a sumar: ")
    return numa + numb

def opRest():
    return numa - numb

def opDiv():
    return round(numa / numb, 4)

def opMult():
    return numa * numb

result = opMult()
print(result)
