from threading import *
from time import sleep

#------ By default execution will be executed by Main Thread
#--- In this scenario we create 2 other threads i.e Thread-1 & Thread-2 by importing threading module and referring to Thread class as parent class

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

#---- Start will internally call run method
t1.start()
sleep(0.2)
t2.start()

#--- join() is used to tell main thread until the t1 & t2 gets finished
t1.join()
t2.join()
print("Bye")