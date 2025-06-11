from tabulate import tabulate
from datetime import datetime
import getpass  # Para ocultar la contraseña al escribirla sin echo
import maskpass   # Para ocultar la contraseña al escribirla con echo

# Base de datos de usuarios (en producción usarías una base de datos real)
usuarios = {
    "admin": {
        "password": "1234",
        "nombre": "Administrador",
        "intentos": 0,
        "bloqueado": False
    }
}

MAX_INTENTOS = 3

def limpiar_pantalla():
    print("\n" * 6)  # Simula limpiar la pantalla

def iniciar_sesion():
    limpiar_pantalla()
    print("=== SISTEMA DE AUTENTICACIÓN ===")
    
    usuario = input("Usuario: ").strip()   # con strip elimina espacios antes y despues del pasw
    
    if usuario not in usuarios:
        print("\nUsuario no encontrado.")
        return False
    
    if usuarios[usuario]["bloqueado"]:
        print("\nCuenta bloqueada. Contacta al administrador.")
        return False
    
    password = maskpass.askpass(" ") # pide la contraseña arrojando * como echo
    #getpass.getpass("Contraseña: ") pide la contraseña sin echo
    
    if usuarios[usuario]["password"] == password:
        usuarios[usuario]["intentos"] = 0  # Reiniciar contador de intentos
        print(f"\nBienvenido, {usuarios[usuario]['nombre']}!")
        return True
    else:
        usuarios[usuario]["intentos"] += 1
        print("\nContraseña incorrecta.")
        
        if usuarios[usuario]["intentos"] >= MAX_INTENTOS:
            usuarios[usuario]["bloqueado"] = True
            print("¡Cuenta bloqueada por demasiados intentos fallidos!")
        
        return False
    
data = []

def ret():
    saldo = 1000
    ret = int(input("Ingrese el monto del retiro:"))
    nsaldo = saldo - ret
    fecha = datetime.now()
    #numoper = numoper + 1
    
    data.append(str(saldo))
    data.append(str(ret))
    data.append(str(nsaldo))
    data.append(str(fecha))
    data.append("1")
    print(f"Saldo actual   : {saldo}")
    print(f"Monto de retiro: {ret}")
    print(f"Nuevo saldo    : {nsaldo}")
    print(f"fecha          : {fecha}")
    #columnas =["SALDO", "RETIRO", "NUEVO SALDO", "FECHA", "FOLIO"]
    #print(tabulate(data, headers=columnas, tablefmt='grid'))    
    return True

def menu_principal():
    while True:
        print("1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if iniciar_sesion():
                print("1. Retiros")  
                print("2. Depositos")
                print("3. Retiros")
                print("4. Salir")

                srv = input("\nSeleccione una opcion: ")
                if srv == "1":
                    ret()
                elif srv == "2":
                    print("modulo en proceso")
                elif srv == "3":
                    print("modulo en proceso")
                else:
                    print("saliendo del sistema.....")
                    break
            #break
        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    print(".....")
    menu_principal()
