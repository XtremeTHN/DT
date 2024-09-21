import json
import socket

from tqdm import tqdm
from .style import info
from .requests import Requests as r

class Server(socket.socket):
    def __init__(self, address="127.0.0.1", port=5050):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)

        self.bind((address, port))
        self.listen()

        self.client, _ = self.accept()

    def recieve(self):
        header = json.loads(self.client.recv(1024))

        match header["request"]:
            case r.FILE:
                progress = tqdm(total=header["bytes-length"], unit="B", unit_scale=True, unit_divisor=1024)
                with open("out.test","wb") as file:
                    while True:
                        chunk = self.client.recv(1024)
                        if chunk == b"":
                            progress.close()
                            break

                        file.write(chunk)
                        progress.update(1024)

                info("Done")
