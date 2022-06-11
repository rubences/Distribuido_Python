from zmq import Context, PUB
import time
import sys
from random import choice

TOPICS = (b"topic1", b"topic2", b"topic3")

context = Context()
socket = context.socket(PUB)
for port in sys.argv[1:]:
    socket.connect(f"tcp://localhost:{port}")

while True:
    msg, topic = input("> ").encode("utf-8"), choice(TOPICS)
    print(f"{topic!r} {msg!r} from port {port}")
    socket.send(topic + b" " + msg)

