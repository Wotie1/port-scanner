
import socket
import threading
import ipaddress
from queue import Queue

TARGET_IP = "127.0.0.1"
START_PORT = 1
END_PORT = 1000
THREAD_COUNT = 50
TIMEOUT = 2

print_lock = threading.Lock()
q = Queue()


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    try:
        result = s.connect_ex((TARGET_IP, port))

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Bilinmeyen servis"

            with print_lock:
                print(
                    f"[OPEN] Port: {port} | "
                    f"Servis: {service}"
                )

    except socket.error as e:
        with print_lock:
            print(f"[ERROR] Port {port}: {e}")

    finally:
        s.close()


def threader():
    while True:
        worker = q.get()

        try:
            portscan(worker)
        finally:
            q.task_done()


def main():
    global TARGET_IP

    try:
        TARGET_IP = str(ipaddress.ip_address(TARGET_IP))

        if not ipaddress.ip_address(TARGET_IP).is_loopback:
            raise ValueError("Yalnızca localhost taranabilir.")

    except ValueError as e:
        print(f"Target error: {e}")
        return

    print(f"Scanning: {TARGET_IP}")
    print("-" * 50)

    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=threader, daemon=True)
        t.start()

    for port in range(START_PORT, END_PORT + 1):
        q.put(port)

    q.join()

    print("-" * 50)
    print("Scanning Completed.")


if __name__ == "__main__":
    main()
