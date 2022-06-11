from zmq import Context, PULL
import sys
from random import randint
from collections import defaultdict

context = Context()
socket = context.socket(PULL)
socket.bind("tcp://*:5561")

data = defaultdict(str)

while True:
    msg_parts = socket.recv().decode("utf-8").split()
    consumer_id, msg = msg_parts[0], " ".join(msg_parts[1:])
    # print(f"{consumer_id!r}: {msg!r}")
    if msg == "STOP":
        print(f"Worker {consumer_id!r} is DONE:", data.pop(consumer_id))
    else:
        data[consumer_id] += msg

