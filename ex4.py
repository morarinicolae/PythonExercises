import threading
#import time

def afiseaza(i):
    print("funcite apelata de thread-ul %i \n" % i)
    #time.sleep(5)
    return

for i in range(5):
    t = threading.Thread(target=afiseaza, args=(i,))
    t.start()
    t.join()

