from zmq import Context, PAIR

context = Context()
socket = context.socket(PAIR)
socket.bind("tcp://*:5556")

while True:
    msg = socket.recv()
    print(f"{msg!r}")
    socket.send(msg)

