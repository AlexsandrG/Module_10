import threading
import time


def passage(iter_obj):
    for i in iter_obj:
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=passage, args=(range(1, 11),))
t2 = threading.Thread(target=passage, kwargs=dict(iter_obj='abcdefghij'))
locker = threading.RLock()

t1.start()
t2.start()

t1.join()
t2.join()