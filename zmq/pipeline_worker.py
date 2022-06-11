from time import sleep
from zmq import Context, PULL, PUSH
import sys
from random import randint

try:
    consumer_id = sys.argv[1].encode("utf-8")
except IndexError:
    consumer_id = str(randint(1, 10000)).encode("utf-8")

context = Context()
socket_in = context.socket(PULL)
socket_in.connect("tcp://localhost:5560")
socket_out = context.socket(PUSH)
socket_out.connect("tcp://localhost:5561")

while True:
    msg = socket_in.recv()
    print(f"{consumer_id!r}: {msg!r}")
    for char in msg:
        socket_out.send(consumer_id + b" " + chr(char).encode("utf-8"))
        sleep(1)
    socket_out.send(consumer_id + b" " + b"STOP")

