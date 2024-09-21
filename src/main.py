import argparse
from modules.client import Client
from modules.server import Server

class Args:
    send: bool
    recieve: bool

    port: int

parser = argparse.ArgumentParser(prog="sdt", description="A program for transfering files through sockets")

parser.add_argument("-s", "--send", action="store_true", help="Sends something to a server.")
parser.add_argument("-r", "--recieve", action="store_true", help="Recieve a file")

parser.add_argument("-p", "--port", default="5050", help="The port of the server or the device to connect")

args: Args = parser.parse_args()

if args.send:
    Client().send_file("test.file")
if args.recieve:
    Server().recieve()
