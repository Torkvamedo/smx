from threading import Thread, Condition
from queue import Queue
import time

class Visitor (Thread):
    def __init__(self,queue_cakes,queue_soups,queue_coffees,mutex_cake,mutex_soup,mutex_coffee,name):
        Thread.__init__(self)
        self.queue_cakes = queue_cakes
        self.queue_soups = queue_soups
        self.queue_coffees = queue_coffees
        self.mutex_cake = mutex_cake
        self.mutex_soup = mutex_soup
        self.mutex_coffee = mutex_coffee
        self.name = name
    def run(self):
        while True:
            self.mutex_cake.acquire()
            while self.queue_cakes.qsize == 0:
                self.mutex_cake.wait()
            self.queue_cakes.get()
            print('visitor' + self.name + 'take cake')
            self.mutex_cake.release()

            self.mutex_soup.acquire()
            while self.queue_soups.qsize == 0:
                self.mutex_soup.wait()
            self.queue_soups.get()
            print('visitor '+ self.name + 'take soup')
            self.mutex_soup.release()

            self.mutex_coffee.acquire()
            while self.queue_coffees.qsize == 0:
                self.mutex_coffee.wait()
            self.queue_coffees.get()
            print('visitor'+ self.name + 'take coffee')
            self.mutex_coffee.release()

            print('visitor is eating ')
            time.sleep(5)

            self.mutex_cake.acquire()
            self.queue_cakes.put('plate')
            print('visitor put empty plate')
            self.mutex_cake.notify()
            self.mutex_cake.release()

            self.mutex_soup.acquire()
            self.queue_soups.put('plate')
            print('visitor put another empty plate')
            self.mutex_soup.notify()
            self.mutex_soup.release()

            self.mutex_coffee.acquire()
            self.queue_coffees.put('cup')
            print('visitor put empty cup')
            self.mutex_coffee.notify()
            self.mutex_coffee.release()

def main():

    mutex_cake = Condition()
    mutex_soup = Condition()
    mutex_coffee = Condition()
    queue_cakes = Queue()
    queue_cakes.put('first cake')
    queue_cakes.put('another cake')
    queue_soups = Queue()
    queue_soups.put('soup')
    queue_soups.put('another soup')
    queue_coffees = Queue()
    queue_coffees.put('a cup of coffee')
    queue_coffees.put('another cup of coffee')
    v1 = Visitor(queue_cakes,queue_soups,queue_coffees,mutex_cake,mutex_soup,mutex_coffee,' v1')


    v1.start()


main()
