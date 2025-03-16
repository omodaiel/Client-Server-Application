import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost and port 12345
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (max 5 queued connections)
server_socket.listen(5)
print("Server is listening on {}:{}".format(*server_address))

try:
    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        client_connection, client_address = server_socket.accept()
        print("Connected to:", client_address)

        try:
            # Receive data from client
            data = client_connection.recv(1024)
            print("Received:", data.decode())
            
            # Process data (convert to uppercase)
            response = data.upper()
            
            # Send response back
            client_connection.sendall(response)
            print("Sent:", response.decode())
            
        finally:
            # Clean up the connection
            client_connection.close()
            print("Connection closed with", client_address)

except KeyboardInterrupt:
    print("\nServer shutting down.")
    server_socket.close()