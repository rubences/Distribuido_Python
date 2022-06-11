from zmq import Context, REP
import time
import sys

try:
    port =  int(sys.argv[1])
except IndexError:
    port = 5556
except ValueError:
    port = 5556

context = Context()
socket = context.socket(REP)
socket.bind(f"tcp://*:{port}")

while True:
    msg = socket.recv()
    print(f"{msg!r} from port {port}")
    socket.send(msg)

