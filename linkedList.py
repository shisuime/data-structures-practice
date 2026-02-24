class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class LinkedList:

    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr += str(itr.data) + "-->"
            itr=itr.next
        print(llstr)     

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

   

    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)   
            self.head=node
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)    
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.getLength():
            raise Exception("index out of bounds")
        
        if index == 0 :
            self.head=self.head.next
            return

        count=0
        itr=self.head
        while itr:
            if count == index -1:
                itr.next=itr.next.next
                break
            count +=1
            itr=itr.next

    def insert_at(self,index,data):
        if index < 0 or index > self.getLength():
            raise Exception("index out of bounds")    

        if index == 0:
            self.insert_at_beginning(data)  
            return 

        itr=self.head
        count =0
        while itr:
            if count == index -1 :
                node=Node(data,itr.next)
                itr.next=node
                break
            count +=1
            itr=itr.next     


if __name__ == '__main__':
    ll=LinkedList()
    # ll.insert_at_beginning(1)
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(4)
    # ll.insert_at_end(0)
    ll.insert_values([1,2,3,4,5,6,67])
    # ll.remove_at(4)
    ll.insert_at(7,432)
    ll.print()