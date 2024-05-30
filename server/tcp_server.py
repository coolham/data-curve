import socketserver
import threading


class TCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            # Receive data from the client
            data = self.request.recv(1024).decode('utf-8')
            if not data:
                break  # Client disconnected

            # Process the received data (e.g., print, save, etc.)
            print(f"Received from {self.client_address}: {data}")

            # Send a response to the client
            response = f"Received your message: {data}".encode('utf-8')
            self.request.sendall(response)

        except Exception as e:
            print(f"Error handling client: {e}")


class TCPServer(socketserver.ThreadingTCPServer):
    def __init__(self, host='localhost', port=8000):
        super().__init__((host, port), TCPRequestHandler)


