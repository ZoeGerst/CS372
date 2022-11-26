#Zoe Gerst
#11/27/2022
#CS 372
#Project 3: Client Socket
#Works cited:
#https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client


import socket

def client_program():

        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))

#       print("Connected to: localhost on port: " + port)

        print("Type /q to quit")
        print("Enter message to send...")

        message = input(">")

        while message.lower().strip() != '/q':

                client_socket.send(message.encode())

                data = client_socket.recv(1024).decode()

                print(data)

                message = input(">")

        client_socket.close()

if __name__ == '__main__':

        client_program()
