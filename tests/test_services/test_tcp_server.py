import time
import socket
import threading
import pytest

from server.tcp_server import TCPServer



# Define a test function to start the server in a separate thread
def start_server():
    server = TCPServer()
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

# Test case to check if the server is running and responding
def test_server_response():
    start_server()

    # Wait for the server to start
    time.sleep(1)

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    # Send a message to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')

    # Close the client socket
    client_socket.close()

    # Check if the response is correct
    assert response == f"Received your message: {message}"

# Run the tests
if __name__ == "__main__":
    pytest.main()