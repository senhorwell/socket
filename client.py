import socket

#inicializa socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecta no servidor endereco:porta
client.connect(('192.168.15.5', 8080))
from_server = ''
data = ''
name = input("Digite seu nome: ")

client.send(bytearray(name,encoding='utf8')) #envia mensagem para servidor

server_name = data = client.recv(4096) #recebe mensagem
print ("\nConectado com " + str(data))

while True:
	data = client.recv(4096) #recebe mensagem do servidor

	if data != from_server:
		from_server = data
		
		print ("\n")
		print(server_name, end = "")
		print(": ",end = "")
		print(from_server)
		
		text = input("\nVoce: ") #leitura de string
		client.send(bytearray(text,encoding='utf8')) #envia mensagem para servidor
client.close() #finaliza conexao com servidor