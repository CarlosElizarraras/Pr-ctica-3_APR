import socket

HOST = "192.168.0.101"
PORT = 9675
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("El servidor está disponible y en espera de solicitudes")

    while True:
        Client_conn, Client_addr = server.accept()
        print("Conectado a", Client_addr)

        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE]:", msg)
        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE-USER]:", msg)

        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE]:", msg)
        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE-PASS]:", msg)

        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE]:", msg)

        case = int.from_bytes(Client_conn.recv(SIZE), 'little')

        if case == 1:
            file = open("Archivos/Messi.txt", "r")
            data = file.read()

            Client_conn.send("Messi.txt".encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE-REQUEST]:", msg)

            Client_conn.send(data.encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)

            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)
            file.close()

        elif case == 2:
            file2 = open("Archivos/Ronaldo.txt", "r")
            data2 = file2.read()

            Client_conn.send("Ronaldo.txt".encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE-REQUEST]:", msg)

            Client_conn.send(data2.encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)

            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)
            file2.close()

        elif case == 3:
            file3 = open("Archivos/Neymar.txt", "r")
            data3 = file3.read()

            Client_conn.send("Neymar.txt".encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE-REQUEST]:", msg)

            Client_conn.send(data3.encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)

            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)
            file3.close()

        elif case == 4:
            file4 = open("Archivos/Chicharito.txt", "r")
            data4 = file4.read()

            Client_conn.send("Chicharito.txt".encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE-REQUEST]:", msg)

            Client_conn.send(data4.encode(FORMAT))
            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]"
                  ":", msg)

            msg = Client_conn.recv(SIZE).decode(FORMAT)
            print("[CLIENTE]:", msg)
            file4.close()
        else:
            break

        msg = Client_conn.recv(SIZE).decode(FORMAT)
        print("[CLIENTE]:", msg)
        Client_conn.close()
        print(Client_addr, "se ha desconectado")


if __name__ == "__main__":
    main()
