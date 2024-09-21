import os
import socket
import threading

from tqdm import tqdm
from modules.style import info
from .requests import Requests as r

class Client(socket.socket):
    def __init__(self, address="127.0.0.1", port=5050):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((address, port))

    def send_req(self, req: str, length=0):
        self.sendall(r.format_request(req, length))

    def send_file(self, f):
        # Getting file size
        size = os.stat(f).st_size

        # Send the file request
        self.send_req(r.FILE, size)

        progress = tqdm(total=size, unit="B", unit_scale=True, unit_divisor=1024)
        with open(f, "rb") as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    self.sendall(b"")
                    self.close()
                    progress.close()
                    break
                self.sendall(chunk)
                progress.update(1024)

        info("Done")
