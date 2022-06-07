import sys
import socket

objetivo = socket.gethostbyname(input("192.168.1.151"))

print("Escaneando objetivo... " + objetivo)

try:
    for port in range(1,163):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} esta abierto")
        s.close()

except:
    print("\n Saliendo..")
    sys.exit(0)