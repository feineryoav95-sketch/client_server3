import socket

my_sock = socket.socket()

#connect to server
try:
    my_sock.connect(("127.0.0.1",1450))
except Exception as e:
    my_sock.close()
    exit(f"server is down - try again {str(e)}")

while True:
    msg = input("enter one of the 4 commands (time,name,rand,exit) ")
    if msg.lower() == "exit":
        break

    try:
        my_sock.send(msg.encode())
        len1 = my_sock.recv(2).decode()
        data = my_sock.recv(int(len1)).decode()
        print(f"server send - {data}")
    except Exception as e:
        print(f"error in receive or sending data {str(e)}")
        break
my_sock.close()
print("Bye Bye, have a great day!")