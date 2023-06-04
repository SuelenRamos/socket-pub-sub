import socket
import threading

clients= []
topics = []
message = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: 
        server.bind(('127.0.0.1', 5050))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor')
    
    while True:
        client, addr = server.accept()
        data = client.recv(1024)
        print(data)

        clients.append(client)
    
        thread = threading.Thread(target= messagesTreatment, args=[client])
        thread.start()



def messagesTreatment(client):
    while True:
        topic = client.recv(1024)
        topics.append(topic)

        msg = client.recv(1024)

        topic_msg = [topic, msg]

        try:
            topic in topics
            indice = message.index(topic)
            message[indice] = topic_msg
        except:
            message.append(topic_msg)

        broadcast(msg)
       

def broadcast(msg):
    while True:
        for clientItem in clients:
            clientItem.send(msg)

main()