from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.container=deque()

    def push(self,data):
        self.container.appendleft(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    

food_order_queue=Queue()

def placeOrders(orders):
    for order in orders:
        print("placing order:",order)
        food_order_queue.push(order)
        time.sleep(0.5)


def serveOrders():
    time.sleep(1)
    while True:
        if food_order_queue.isEmpty():
            print("all placed orders are served")
            return
        order=food_order_queue.pop()
        print("serving :",order)
        time.sleep(2)



if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=placeOrders, args=(orders,))
    t2=threading.Thread(target=serveOrders)


    t1.start()
    t2.start()

