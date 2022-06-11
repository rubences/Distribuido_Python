from zmq import Context, PUSH
import time
import sys
from random import choice

context = Context()
socket = context.socket(PUSH)
socket.bind("tcp://*:5560")

while True:
    msg = input("> ").encode("utf-8")
    if not msg:
        break
    print(f"{msg!r} from producer")
    socket.send(msg)

