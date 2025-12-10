import threading
import time

playroom = threading.Semaphore(2)

def enter_player(num):
    print(f"Player {num} is waiting...")
    playroom.acquire()
    print(f"Player {num} entered the playroom")
    time.sleep(1)
    print(f"Player {num} left the playroom")
    playroom.release()

threads = []

for i in range(5):
    t = threading.Thread(target=enter_player, args=(i+1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()