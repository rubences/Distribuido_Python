from zmq import Context, PUB
import time
import sys
from random import choice

TOPICS = (b"topic1", b"topic2", b"topic3")

try:
    port =  int(sys.argv[1])
except IndexError:
    port = 5556
except ValueError:
    port = 5556

context = Context()
socket = context.socket(PUB)
socket.bind(f"tcp://*:{port}")

while True:
    msg, topic = input("> ").encode("utf-8"), choice(TOPICS)
    print(f"{topic!r} {msg!r} from port {port}")
    socket.send(topic + b" " + msg)

