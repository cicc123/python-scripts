import threading
import time
from multiprocessing import Process

def tstart(arg):
    time.sleep(1)
    print("%s running...." % arg)

if __name__ == '__main__':
    t1 = Process(target=tstart, args=('This is thread 1',))
    t2 = Process(target=tstart, args=('This is thread 2',))
    while True:
        t1.start()
        t2.start()
    print("This is main function")