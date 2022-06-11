from zmq import Context, SUB, SUBSCRIBE
import sys

context = Context()
socket = context.socket(SUB)
for port in sys.argv[1:]:
    socket.connect(f"tcp://localhost:{port}")

while True:
    topic = input("topic: ")
    if not topic:
        break
    socket.subscribe(topic)

while True:
    msg_parts = socket.recv().split()
    topic, msg = msg_parts[0], " ".join(m.decode("utf-8") for m in msg_parts[1:])
    print(f"{topic}: {msg}")

