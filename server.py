import socket
import json
#import lib

server_sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM, # SOCK_DGRAM
        proto = 0) #создаем сокет

server_sock.bind(("127.0.0.1", 12345)) #привязываем сокет к конкретному ip(127.0.0.1 - адрес используется 
                                       #для соединения с одним и тем же компьютером)
server_sock.listen(5) #создаем слушающий сокет(ждём подключение); 5 - очередь подключения

server_sock.settimeout(20) 

while 1:

    sock, addr = server_sock.accept() #addr - адрес клиента который подключился

    prog = \
        {
            "+" : (15, 20),
            "-" : (5, 3),
            "*" : (3.5, 10),
            "/" : (16, 8)
        }
    
    prog_json = json.dumps(prog) #преобразовываем словарь в строку
    prog_byte = prog_json.encode() #преобразовываем в байты
    
    sock.send(prog_byte) #отправляем
    
    result_byte = sock.recv(1024) #ждем результат
    result = json.loads(result_byte.decode())#преобразуем из байт в строку
    #result = lib.main_loop(sock, prog)
    

    print(result)