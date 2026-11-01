
import socket
import threading
from queue import Queue
from datetime import datetime

target = input("Target IP (e.g., google.com): ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror as e:
    print(f"IP çözümleme hatası: {e}")
    exit()

print_lock = threading.Lock()

print(f"Scanning: {target_ip}")
print("-" * 50)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    try:
        result = s.connect_ex((target_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Bilinmeyen servis"

            with print_lock:
                print(f"✅ Port {port} OPEN | Servis: {service}")

    except socket.error as e:
        with print_lock:
            print(f"❌ Port {port} hata: {e}")

    finally:
        s.close()


def threader():
    while True:
        worker = q.get()

        try:
            portscan(worker)
        finally:
            q.task_done()


q = Queue()

for x in range(50):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 1001):
    q.put(worker)

q.join()

print("-" * 50)
print("Scanning Completed.")
