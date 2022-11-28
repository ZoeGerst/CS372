#Zoe Gerst
#11/27/2022
#CS 372
#Project 3: Server Socket
#Works cited:
#https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client


import socket


def server_program():

	#connect to host and address port
	host = socket.gethostname()
	port = 5000

	server_socket = socket.socket()

	server_socket.bind((host, port))

	#listen for client
	server_socket.listen(2)

	conn, address = server_socket.accept()

	#tells user what host and port number they are on
	print("Server listening on: localhost on port: " + str(port))

	#prints IP address
	print("Connected by " + str(address))

	print("Waiting for message")

	print("Type /q to quit")
	print("Enter message to send...")

	#if the server correctly accepts the client
	while True:

		#receives messages from client
		data = conn.recv(1024).decode()

		#if the messages are not received
		if not data:
			
			break

		print(str(data))

		data = input('>')

		#if messages is not /q then the server will continue to send messages to client
		if data.lower().strip() != '/q':

			conn.send(data.encode())

		#Ends program if the user types /q
		elif data.lower().strip() == '/q':

			break
			

	conn.close()

if __name__ == '__main__':
	
	server_program()
