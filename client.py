import socket
import json
#import lib

def div(x, y):
    return x/y

sock = socket.socket(
        family = socket.AF_INET,
        type = socket.SOCK_STREAM, # SOCK_DGRAM
        proto = 0) #создаем сокет

sock.connect(("127.0.0.1", 12345)) #подключаемся к удаленному серверу

data_byte = sock.recv(1024) #читаем данные из сокета
data = json.loads(data_byte.decode()) #преобразуем в строку далее в словарь

###########################

funcs = \
      {
          "+" : lambda x, y: x + y,
          "-" : lambda x, y: x - y,
          "*" : lambda x, y: x * y,
          "/" : div
      }     
result = {}

for f in data:
    
    result[f] = funcs[f](data[f][0], data[f][1])

###########################

result_byte = json.dumps(result).encode() #перобразуем в байты
sock.send(result_byte) #отправляем