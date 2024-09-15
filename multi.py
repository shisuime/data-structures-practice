# import threading
# import time
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.buffer=deque()


#     def enqueue(self,val):
#         self.buffer.appendleft(val)


#     def dequeue(self):
#         if len(self.buffer)== 0:
#             print("empty")
#             return
#         return self.buffer.pop()    

# food_queue=Queue()
# orders_done=False

# def placeOrder(orders):
#     global orders_done
#     for order in orders:
#         print("placing order:",order)
#         food_queue.enqueue(order)
#         time.sleep(0.5)
#     orders_done=True

# def serveOrder():
#     time.sleep(1)
#     while True:
#         order=food_queue.dequeue()
#         if order is None:
#             if orders_done:
#                 print("served all")
#                 break
#             else:
#                 time.sleep(1)
#                 continue
#         print("serving :",order)
#         time.sleep(2)        


# orders = ['pizza','samosa','pasta','biryani','burger']
# t1=threading.Thread(target=placeOrder, args=(orders,))
# t2=threading.Thread(target=serveOrder)

# t1.start()
# t2.start()


# import threading
# import time
# from collections import deque

# class Queue:
#     def __init__(self):
#         self.buffer=deque()


#     def enqueue(self,val):
#         self.buffer.appendleft(val)


#     def dequeue(self):
#         if len(self.buffer)== 0:
#             print("empty")
#             return
#         return self.buffer.pop()    

#     def front(self):
#         return self.buffer[-1]
    


# def produceBinary(n):
#     binaryQueue=Queue()
    
#     binaryQueue.enqueue("1")
#     for i in range(n):
#         front=binaryQueue.front()
#         print("front :",front)
#         binaryQueue.enqueue(front + "1")
#         binaryQueue.enqueue(front + "0")

#         binaryQueue.dequeue()
    
# produceBinary(10)