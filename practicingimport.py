# import numpy as np
# import pandas as pd


# nparray= np.array([1,2,3,4])

# print(nparray,"nparray")

# zeroArray=np.zeros((5,4))
# print(zeroArray,"zeroArray")

# oneArray=np.ones((5,4))
# print(oneArray,"oneArray")


# emptyArray=np.empty((5,4))
# print(emptyArray,"emptyArray")



# arrangeArray=np.arange((12))
# print(arrangeArray,"arrangeArray")


# print(arrangeArray.reshape(6,2),"reshaping")



# linspaceArray=np.linspace(1,4,3)
# print(linspaceArray,"linspacearray")

# threeDArray=np.arange(8).reshape(2,2,2)
# print(threeDArray,"3DArray")

# testArray=np.arange(20)
# print(testArray,"testArray")
# print(testArray.ravel(),"ravel")
# testArray.resize(2,6)
# print(testArray,"resize")

# b=np.hsplit(testArray,3)
# print(b,"hsplit")

# c=np.hstack(arrangeArray)

# print(c,"hstack")


# arrayTest=[2200,2350,2600,2130,2190]

# extraEXP=arrayTest[1]-arrayTest[0]
# totalEXP=arrayTest[1]+arrayTest[0]+arrayTest[0]

# print("stats",2000 in arrayTest)
# arrayTest.append(1980)
# print(arrayTest)
# arrayTest[3]=arrayTest[3]+200
# print(arrayTest)

# heros=['spider man','thor','hulk','iron man','captain america']
# length=len(heros)
# print(length)
# heros.append("black panther")
# print(heros)
# heros.remove("black panther")
# heros.remove("hulk")
# heros.append("dr strange")
# print(heros)
# print(dir(heros))
# heros.sort()
# print(heros)

# maxnumber=int(input("enter max number"))
# list1=[]

# for i in range(0,maxnumber+1):
#     if(i%2 !=0):
#         list1.append(i)

# print(list1)


#  Node {data:none,next:none}                                                            itr                           
# LinkedList  {head:none}  insertatBegining node {data:data,next:none} ->  Linkedlist {head:{data:data,next:none}} \\  {data:data, next:{data:data,next:none}} \\ 
# {itr:{data:data,next:{data:data,next:{data:data,next:none}}}}

# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insert_at_begining(self,data):
#         node=Node(data,self.head)        
#         self.head=node

#     def print(self):
#         if self.head is None:
#             print("linked list empty")
#             return

#         itr=self.head
#         likedliststring=""

#         while itr:
#             likedliststring += str(itr.data) + "-->"

#             itr=itr.next    





# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertInBegining(self,data):
#         node=Node(data,self.head)
#         self.head=node
#     def insertatEnd(self,data):
#         if self.head is None:  
#             self.head=Node(data,None)
#             return
        
#         itr=self.head
#         while itr.next:
#             itr=itr.next 
            
#         itr.next= Node(data,None)

#     def insertValues(self,dataList):
#         self.head=None
#         for data in dataList:
#             self.insertatEnd(data)

#     def print(self):
#         if self.head is None:
#             print("empty linked list")
#             return

#         iterator=self.head
#         linkedlistString=""
#         # print(self.,"self")
#         while iterator:
#             linkedlistString= linkedlistString + str(iterator.data) + "-->"

#             iterator=iterator.next

#         print(linkedlistString)

#     def get_length(self):
#         count=0
#         itr=self.head
#         while itr:
#             count+=1
#             itr=itr.next 
#         return count       

#     def remove_at(self,index):
#         if index < 0 or index >=self.get_length():
#             raise Exception("Invalid Index")
#         if index==0:
#             self.head= self.head.next
#             return
#         count=0
#         itr=self.head
#         while itr:
#             if count == index -1:
#                 itr.next=itr.next.next
#                 break

#             itr=itr.next
#             count+=1
#     def insert_at(self,index,data):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid Index")
#         if index == 0:
#             self.insertInBegining(data)
#             return
        
#         if index == self.get_length():
#             self.insertatEnd(data)
#             return
#         count = 0
#         itr=self.head
#         while itr:
#             if count == index -1:
#                 node=Node(data,itr.next)
#                 itr.next=node
#                 break
#             itr=itr.next
#             count +=1

#     def insert_after_values(self,data_after,data_to_insert):
#         itr=self.head
#         while itr:
#             if itr.data == data_after:
#                 node=Node(data_to_insert,itr.next)
#                 itr.next=node
#                 break
#             itr=itr.next
#     def remove_by_value(self,data_to_remove):
#         if self.head is None:
#             return
#         if self.head.data == data_to_remove:
#             self.head=self.head.next

#         prev=None
#         current=self.head
#         while current:
#             if current.data == data_to_remove:
#                 if prev:
#                     prev.next=current.next
#                 return    
#             prev=current
#             current=current.next
# if __name__ == "__main__":

#     lnkObj=LinkedList()
#     lnkObj.insertInBegining(45)
#     lnkObj.insertInBegining(50)
#     lnkObj.insertInBegining(55)
#     lnkObj.insertInBegining(60)
#     lnkObj.insertatEnd(70)
#     lnkObj.insertValues(["apple","mango","coconut","banana"])
#     # lnkObj.remove_at(2)
#     lnkObj.insert_at(4,"nig")
#     lnkObj.print()
#     print("length",lnkObj.get_length())
#     lnkObj.insert_after_values("nig","jackfruit")
#     lnkObj.remove_by_value("coconut")
#     lnkObj.print()



# class Node:
#     def __init__(self,data=None, prev=None, next=None):
#         self.data=data
#         self.prev=prev
#         self.next=next


# class DLinkedList:
#     def __init__(self):
#         self.head=None

#     def print_forward(self)




class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
          
        curr=self.head 
        while curr.next is not None:
            curr=curr.next
        curr.next= new_node   

    def findLength(self):
        curr=self.head
        total=0
        while curr is not None:
            total=total+1
            curr=curr.next
            
        return total               

    def show(self):
        elements=[]
        curr=self.head
        while curr is not None:
            
            elements.append(curr.data)
            curr=curr.next
        print ("elements",elements)    

    def get(self,index):
        
        if (index < 0 or index >= self.findLength()):
            print("out of bounds")
            return None
        curr_node=self.head
        curr_index=0
        while curr_node is not None:
            
            if(curr_index==index):
                return curr_node.data
            curr_index=curr_index+1
            curr_node=curr_node.next
        return None    

    def erase(self,index):
        if(index<0 or index >= self.findLength()):
            print("out of bounds")
            return
        
        if index == 0:
            if self.head is not None:
                self.head=self.head.next
            return
        
        curr_index=0
        curr_node=self.head
       

        while curr_node is not None and curr_node.next is not None:
            if curr_index == index -1:
                curr_node.next=curr_node.next.next
                return

            curr_node=curr_node.next
            curr_index +=1 






objLinkedList= LinkedList()

objLinkedList.append(1)
objLinkedList.append(2)
objLinkedList.append({"new":"hi"})
# objLinkedList.show()
variable=objLinkedList.findLength()
print("total",variable)
got=objLinkedList.get(1)
print("gotcha",got)
objLinkedList.erase(0)
objLinkedList.show()

