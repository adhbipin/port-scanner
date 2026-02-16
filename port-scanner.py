import socket
target = input("Enter IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))
for port in range(start, end + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    if sock.connect_ex((target, port)) == 0:
        print(f"Port {port} is open")
    sock.close()