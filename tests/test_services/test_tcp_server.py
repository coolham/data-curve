import socket
import threading
import pytest

from server.tcp_server import TCPServer, TCPRequestHandler

@pytest.fixture
def test_server_startup():
    with TCPServer() as server:
        assert server.server_address == ('localhost', 8000)  # Default port

@pytest.fixture
def test_client_connection(monkeypatch):
    # Mock the `handle` method to capture received data
    def mock_handle(self):
        self.received_data = self.request.recv(1024).decode('utf-8')

    monkeypatch.setattr(TCPRequestHandler, 'handle', mock_handle)

    with TCPServer() as server:
        # Start the server in a separate thread
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()

        # Connect to the server from a client
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(server.server_address)
            client_socket.sendall(b"Hello from client!")

        # Wait for the server to process the data
        server_thread.join(timeout=1)
        
        # Create a TCPRequestHandler instance to access the mocked received_data
        handler = TCPRequestHandler()

        # Check if the server received the correct data
        assert handler.received_data == "Hello from client!"

