from zmq import Context, REQ
import sys

context = Context()
socket = context.socket(REQ)
for port in sys.argv[1:]:
    socket.connect(f"tcp://localhost:{port}")

while True:
    msg = input("> ")
    socket.send_string(msg)
    msg = socket.recv()
    print("echo:", msg)

