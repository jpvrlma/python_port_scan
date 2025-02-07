import socket

ip = input("Digite o IP: ")

for porta in range (0,65535):
    meuSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    resposta = meuSocket.connect_ex((ip,porta))
    if (resposta == 0):
        print(f"Porta {porta}: Aberta!")
    meuSocket.close()
print("Scan finalizado")