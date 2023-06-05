import socket
import threading

clientsSub= []
clientPub = []
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
        pubOrSub = client.recv(1024)

        if pubOrSub == b'publisher':
            clientPub.append(client)
            thread = threading.Thread(target= messagesTreatment, args=[client, addr])
            thread.start()
        elif pubOrSub==b'subscriber':
            clientsSub.append(client)
            thread = threading.Thread(target= messagesTreatment, args=[client, addr])
            thread.start()
        
        
    """
    while True:
        data = client.recv(1024)
        print(data)"""
    



def messagesTreatment(client, addr):
    topic = client.recv(1024)
    topics.append(topic)

    while True:
        msg = client.recv(1024)
        topic_msg = [topic, msg]

        for c in clientsSub:
            print(f"{c}")
            c.sendall(msg)

        try:
            if topic in topics:
                indice = message.index(topic)
                message[indice] = topic_msg
        except:
            message.append(topic_msg)


main()