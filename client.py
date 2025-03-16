import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

try:
    # Send data
    message = input("Enter message to send: ")
    client_socket.sendall(message.encode())
    print("Sent:", message)

    # Receive response
    response = client_socket.recv(1024)
    print("Received:", response.decode())

finally:
    # Clean up the connection
    client_socket.close()