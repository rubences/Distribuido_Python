from zmq import Context, PAIR

context = Context()
socket = context.socket(PAIR)
socket.connect("tcp://localhost:5556")

while True:
    msg = input("> ")
    if not msg:
        break
    socket.send_string(msg)
    msg = socket.recv()
    print("echo:", msg)

socket.disconnect("tcp://localhost:5556")

