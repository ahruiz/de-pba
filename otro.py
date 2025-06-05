import getpass  # Para ocultar la contraseña al escribirla sin echo
import maskpass   # Para ocultar la contraseña al escribirla con echo

# Base de datos de usuarios (en producción usarías una base de datos real)
usuarios = {
    "admin": {
        "password": "AdminSecure123",
        "nombre": "Administrador",
        "intentos": 0,
        "bloqueado": False
    },
    "juan": {
        "password": "JuanClave456",
        "nombre": "Juan Pérez",
        "intentos": 0,
        "bloqueado": False
    }
}

MAX_INTENTOS = 3

def limpiar_pantalla():
    print("\n" * 5)  # Simula limpiar la pantalla

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

def menu_principal():
    while True:
        print("\n1. Iniciar sesión")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if iniciar_sesion():
                # Área restringida - solo para usuarios autenticados
                input("\nPresiona Enter para continuar...")
                # Aquí iría el código de la aplicación principal
                break
        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    print(".....")
    menu_principal()
