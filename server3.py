import socket
import time
import random
#create the server
server_soc = socket.socket()
server_soc.bind(("0.0.0.0",1450))
server_soc.listen(4)



while True:
    client_soc, addr = server_soc.accept()
    print(f"{addr[0]} - connected")
    while True:
        try:
            data = client_soc.recv(4).decode()
            command = data.lower()
            if command not in ["time","name","rand","exit"]:
                break
            print(f"getting data - {data}")

            if command == "time":
                time_sec = time.time()
                current_time = time.localtime(time_sec)
                ret_ans = time.strftime("%H:%M", current_time)
            elif command == "name":
                ret_ans = "Yoav's simple server"
            else:
                ret_ans = str(random.randint(1,11))



            len1 = str(len(ret_ans)).zfill(2)

            client_soc.send(len1.encode())
            client_soc.send(ret_ans.encode())
        except Exception as e:
            print(f"error in recv/send {str(e)}")
            break
    print(f"{addr[0]} - disconnected")
    client_soc.close()