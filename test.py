import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 11111))
    while True:
        data = input("enter your input here:")
        length = str(len(data))
        filledlength = length.zfill(2)
        data = filledlength + data
        s.send(data.encode())
        length = s.recv(2).decode()
        if not length.isnumeric:
            print("WRONG PROTOCOL")
        message = s.recv(int(length)).decode()
        if message[:2] == "no":
            print("connection closed")
            s.close
            break
        else:
            print(message)


if __name__ == "__main__":
    main()
