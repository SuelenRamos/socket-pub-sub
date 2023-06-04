import socket

HOST = '127.0.0.1'    # The remote host
PORT = 5050              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'publisher')
    
    topic = input('Tópico: ')
    s.sendall(bytes(topic, 'utf-8'))

    while True:
        msg = input('Mensagem: ')
        s.sendall(bytes(msg, 'utf-8'))
    
   
