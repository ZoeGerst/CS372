#Zoe Gerst
#11/27/2022
#CS 372
#Project 3: Client Socket
#Works cited:
#https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client


import socket

def client_program():

	#needs to run on the same program as server
	host = socket.gethostname()
	port = 5000

	client_socket = socket.socket()
	client_socket.connect((host, port))

	#shows what host and port it is connected to
	print("Connected to: localhost on port: " + str(port))

	print("Type /q to quit")
	print("Enter message to send...")

	message = input(">")

	#While the server's message is not equal to /q
	while message.lower().strip() != '/q':
		
		#first to send a messages
		client_socket.send(message.encode())

		#server's response
		data = client_socket.recv(1024).decode()

		print(data)

		#new message
		message = input(">")		

	client_socket.close()

if __name__ == '__main__':

	client_program()
