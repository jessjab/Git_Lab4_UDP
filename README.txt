Program Title: UDP SOCKET Program

Modules and their IOs for this program:

		UDP_client: keyboard input = Server IP Adress, UDP Port Number, Client Number, Encrypt Key- ---------->Press enter and "Input" wil then appear,so type your message.
				   example = "127.0.0.1 6789 0 3"----------------------------------------------------->Press enter 
					     Input: "This is the message I am typing." -------------------------------> Press enter

		UDP_server: keyboard input= UDP Port Number
				   example = "6789"--------------------------------------->Press enter

		*RUN SERVER THEN CLIENT*

What this program does:

	1. Sets up a socket between multiple clients and a server, where the server waits and listens for messages from the client.
	2. The client accepts the above defined inputs (server's IP address, port number, user's message) from the keyboard and encrypts the user's message.
	3. The client then sends data to the server, including the clients number, the timestamp, the client's IP address, and the encrypted user's message. 
	4. The client then waits to recieve data back from the server. 
	

	5. The server accepts the above defined inputs (the port number). 
	6. When the server recieves the data from the client(s), the server picks out the users message and decryptes it.
	7. The server then sends the client that just talked the last 5 messages it had recieved including the clients number, the timestamp, the client's IP address, and the decrypted user's message

What this program assumes:

	The client already contains the keys to encrypt the user's messages
	The server already contains the keys to decrypt each of the user's decrypted messages from each of the different clients.
	(Therefore, an error is thrown if the clients key does not exist at the server.)
