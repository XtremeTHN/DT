import argparse
from modules.client import Client
from modules.server import Server

class Args:
    send: bool
    recieve: bool

    address: str
    port: int

parser = argparse.ArgumentParser(prog="sdt", description="A program for transfering files through sockets")

parser.add_argument("-s", "--send", action="store", help="Sends something to a server.")
parser.add_argument("-r", "--recieve", action="store_true", help="Recieve a file")

parser.add_argument("-a", "--address", default="127.0.0.1", help="The address of the server to create/connect")
parser.add_argument("-p", "--port", default="5050", type=int, help="The port of the server or the device to connect")

args: Args = parser.parse_args()

if args.send:
    c = Client(args.address, args.port)
    c.send_file(args.send)

if args.recieve:
    Server().recieve()
