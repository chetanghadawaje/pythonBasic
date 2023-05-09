import threading
import queue

my_queue = queue.Queue()


def worker():
    for i in range(5):
        my_queue.put(i)
        print(f"Added {i} to the queue")


thread1 = threading.Thread(target=worker())
thread2 = threading.Thread(target=worker())

thread1.start()
thread2.start()

# thread1.join()
# thread2.join()

while not my_queue.empty():
    item = my_queue.get()
    print(f"Got {item} from the queue")
