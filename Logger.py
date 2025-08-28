import socket
from datetime import datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, _ = sock.recvfrom(4096)
    msg = data.decode(errors='ignore')
    now = datetime.now().strftime("%H:%M:%S")
    print(f"SALogger [{now}] {msg}")
