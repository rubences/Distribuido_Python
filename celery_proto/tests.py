from time import sleep, time
from tasks import add


def test():
    t0 = time()
    for i in range(12):
        result = add.delay(i, i)
        while not result.ready():
            sleep(0.001)
        print(time()-t0, result.get())

if __name__ == "__main__":
    test()

