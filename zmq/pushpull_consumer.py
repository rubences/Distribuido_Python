from zmq import Context, PULL
import sys
from random import randint

try:
    consumer_id = sys.argv[1]
except IndexError:
    consumer_id = randint(1, 10000)

context = Context()
socket = context.socket(PULL)
socket.connect(f"tcp://localhost:5556")

while True:
    msg = socket.recv()
    print(f"{consumer_id}: {msg}")

