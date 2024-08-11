import socket
import pickle


client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(('127.0.0.1' , 8500))
data = ['foroozan' , 1 ,2 , 4 , [8,7,6]]
pickle_data = pickle.dumps(data)

client.send(pickle_data)

client.close()