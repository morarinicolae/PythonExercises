from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.mesaj = "initializarea thread\n"

    def afisare(self):
        print(self.mesaj)

    def run(self):
        print("Start thread ...")
        x=0
        while (x<10):
            self.afisare()
            sleep(2)
            x +=1
        print("END thread")

print("Start process ...")
thd = MyThread()
thd.start()
print("END process ...")
