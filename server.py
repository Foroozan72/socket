import socket
from threading import Thread
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8500))

server.listen()

def handel_client(connection: socket.socket, address: tuple) -> None:
    print(f'client connected : {address}')
    while True:
        data = connection.recv(1024)
        if not data:
            print('connection closed.')
            break
        try:
            pickle_data = pickle.loads(data)
            print(pickle_data)
        except (pickle.UnpicklingError, EOFError):
            print('Received data is not in the expected pickle format.')
            break

while True:
    connection, address = server.accept()
    Thread(target=handel_client, args=(connection, address)).start()