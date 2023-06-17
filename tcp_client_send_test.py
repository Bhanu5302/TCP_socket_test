import socket
import time

HOST = "192.168.1.100"
PORT = 10001
a =0
while a == 0:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        time.sleep(1)
        txt = "bhanu" +'\n'
        #txt = "popup(\”Messages\”, title=\”The Headline the Blue box\”, blocking=True)"
        msg = txt.encode("utf8")
        s.sendall(msg)
        time.sleep(0.2)
        data = s.recv(4096)
        print(f"Received {data!r}")
        a = 1
        # print("\n\n 2.Client received: ", data.decode("utf8"))


        # print(data.decode("UTF-8"))