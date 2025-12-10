import threading
import time

def worker(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed.")