#https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/

import socket

#inicializa socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#mapeamento do endereco:porta do servidor
serv.bind(('192.168.15.5', 8080))

#escuta a porta
serv.listen(5)

name = input("Digite seu nome: ")

while True:
    #aceita conexao retornando um descritor
    conn, addr = serv.accept()

    #inicializacao de string
    from_client = ''
    data = ''
    

    conn.send(bytearray(name,encoding='utf8')) #envio de mensagem para cliente

    client_name = data = conn.recv(4096) #recebe mensagem
    print ("\nConectado com ", end = "")
    print(data)
    text = input("\nVoce: ")
    conn.send(bytearray(text,encoding='utf8')) #envio de mensagem para cliente
    
    while True:
        
        data = conn.recv(4096) #recebe mensagem

        if not data: break #caso de erro

        if data != from_client:
            from_client = data
            
            print ("\n")
            print(client_name, end = "")
            print(": ", end = "")
            print(from_client)

            text = input("\nVoce: ")
            conn.send(bytearray(text,encoding='utf8')) #envio de mensagem para cliente

    conn.close() #finaliza conexao para com cliente