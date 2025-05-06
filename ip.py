import socket
EQ = "DESKTOP-30N5R6C"
def obtener_ip_remota(EQ):
    try:
        return socket.gethostbyname(EQ)
    except socket.error as err_msg:
        print(f"{EQ}: {err_msg}")

obtener_ip_remota(EQ)