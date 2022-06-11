from zmq import Context, SUB, SUBSCRIBE
from random import sample, randint
import sys

TOPICS = (b"topic1", b"topic2", b"topic3")

try:
    port =  int(sys.argv[1])
except IndexError:
    port = 5556
except ValueError:
    port = 5556

context = Context()
socket = context.socket(SUB)
socket.bind(f"tcp://*:{port}")

for topic in sample(TOPICS, randint(2, len(TOPICS))):
    print(f"Subscribe to {topic}")
    socket.setsockopt(SUBSCRIBE, topic)

while True:
    msg_parts = socket.recv().split()
    topic, msg = msg_parts[0], " ".join(m.decode("utf-8") for m in msg_parts[1:])
    print(f"{topic}: {msg}")

