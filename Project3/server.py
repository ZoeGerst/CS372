#Zoe Gerst
#11/27/2022
#CS 372
#Project 3: Server Socket
#Works cited:
#https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client


import socket


def server_program():

        host = socket.gethostname()
        port = 5000

        server_socket = socket.socket()

        server_socket.bind((host, port))

        server_socket.listen(2)

        conn, address = server_socket.accept()

#       print("Server listening on: localhost on " + port)

        print("Connected by " + str(address))

        print("Waiting for message")

        print("Type /q to quit")
        print("Enter message to send...")

        while True:

                data = conn.recv(1024).decode()

				if not data:

                        break

                print(str(data))

                data = input('>')

                if data.lower().strip() != '/q':

                        conn.send(data.encode())

                elif data.lower().strip() == '/q':

                        break


        conn.close()

if __name__ == '__main__':

        server_program()
