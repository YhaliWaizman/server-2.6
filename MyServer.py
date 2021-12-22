import socket
import datetime
import random


def main():
    MyServer = socket.socket()
    MyServer.bind(("0.0.0.0", 11111))
    MyServer.listen()
    print("Server is running...")
    client, address = MyServer.accept()
    print("Connection from: ", address)
    while True:
        length = client.recv(2).decode()
        if not length.isnumeric:
            print("WRONG PROTOCOL")
        data = None
        data = client.recv(int(length)).decode()
        if data[:4] == "TIME":
            time = datetime.datetime.now().strftime("%H:%M:%S")
            retval = str(len(str(time))).zfill(2) + time
            client.send(retval.encode())
        elif data[:5] == "WHORU":
            retval = str(len(f"my name is {socket.gethostname()}")).zfill(
                2) + f"my name is {socket.gethostname()}"
            client.send(retval.encode())
        elif data[:4] == "RAND":
            retval = "01" + str(random.randrange(1, 11))
            client.send(retval.encode())
        elif data[:4] == "EXIT":
            client.send(("02" + "no").encode())
            break
        else:
            client.send(("14" + "WRONG PROTOCOL").encode())


if __name__ == "__main__":
    main()
