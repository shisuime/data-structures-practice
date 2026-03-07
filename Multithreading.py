import time
import threading

def calc_square(array):
    for num in array:
        time.sleep(0.2)
        print("squares",num*num)



def calc_cube(array):
    for num in array:
        time.sleep(0.2)
        print("cubes",num*num*num)        



arr=[1,2,3,4,5]


t=time.time()


t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))

t1.join()
t2.join()

print("done in :",time.time()-t)


