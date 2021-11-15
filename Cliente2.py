import socket

HOST = "192.168.0.101"
PORT = 9665
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print("Se ha conectado al servidor")

    seguir = True
    while (seguir):
        print("Menu de Solicitudes. Escoge un número:")
        print("1.USER\n2.PASS\n3.REQUEST\n4.QUIT")
        case = int(input("Opcion: "))
        if case == 1:
            client.send("USER".encode(FORMAT))
            usuario = input("Ingrese su nombre de usuario:")
            if usuario == "Carlos":
                client.send(usuario.encode(FORMAT))
                print("Usuario correcto")
            else:
                print("El usuario es incorrecto")
        elif case == 2:
            client.send("PASS".encode(FORMAT))
            contraseña = input("Ingrese su contraseña:")
            if contraseña == "12345":
                client.send(contraseña.encode(FORMAT))
                print("Contraseña correcta")
            else:
                print("La contraseña es incorrecta")

        elif case == 3:
            client.send("REQUEST".encode(FORMAT))
            print("¿Qué archivo desea recibir?\n1.Messi.txt\n2.Ronaldo.txt\n3.Neymar.txt\n4.Chicharito.txt")
            case = int(input("Archivo:"))
            caseb = case.to_bytes(1, 'little')
            client.send(caseb)
            if case == 1:
                client.send("Messi.txt".encode(FORMAT))
                filename = client.recv(SIZE).decode(FORMAT)
                print("Se recibió", filename)
                file = open(filename, "w")
                client.send("Archivo recibido".encode(FORMAT))

                data = client.recv(SIZE).decode(FORMAT)
                print("Datos del archivo recibido")
                file.write(data)
                client.send("Datos recibidos".encode(FORMAT))

                file.close()
            elif case == 2:
                client.send("Ronaldo.txt".encode(FORMAT))
                filename2 = client.recv(SIZE).decode(FORMAT)
                print("Se recibió", filename2)
                file2 = open(filename2, "w")
                client.send("Archivo recibido".encode(FORMAT))

                data2 = client.recv(SIZE).decode(FORMAT)
                print("Datos del archivo recibido")
                file2.write(data2)
                client.send("Datos recibidos".encode(FORMAT))

                file2.close()
            elif case == 3:
                client.send("Neymar.txt".encode(FORMAT))
                filename3 = client.recv(SIZE).decode(FORMAT)
                print("Se recibió", filename3)
                file3 = open(filename3, "w")
                client.send("Archivo recibido".encode(FORMAT))

                data3 = client.recv(SIZE).decode(FORMAT)
                print("Datos del archivo recibido")
                file3.write(data3)
                client.send("Datos recibidos".encode(FORMAT))

                file3.close()
            elif case == 4:
                client.send("Chicharito.txt".encode(FORMAT))
                filename4 = client.recv(SIZE).decode(FORMAT)
                print("Se recibió", filename4)
                file4 = open(filename4, "w")
                client.send("Archivo recibido".encode(FORMAT))

                data4 = client.recv(SIZE).decode(FORMAT)
                print("Datos del archivo recibido")
                file4.write(data4)
                client.send("Datos recibidos".encode(FORMAT))

                file4.close()

            else:
                break
        elif case == 4:
            client.send("QUIT".encode(FORMAT))
            client.close()
            exit()
        else:
            print("Opcion no valida\n")
        Option = int(input("1.Continuar\n2.Salir\nElige una opcion:"))
        if Option == 1:
            seguir = True
        else:
            seguir = False
            client.close()


if __name__ == "__main__":
    main()
