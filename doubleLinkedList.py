class Node:
    def __init__(self,prev=None,data=None,next=None,):
        self.data=data
        self.prev=prev
        self.next=next

class DLinkedList:
    def __init__(self):
        self.head=None        

    def insert_at_begining(self,data):
        if self.head is None:
            self.head=Node(None,data,self.head)
            return
        else:
            node=Node(None,data,self.head)
            self.head.prev=node
            self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(None,data,None)
            return
        else:
           itr=self.head
           while itr.next:
               itr=itr.next
           itr.next=Node(itr,data,None)


    def printAll(self):
        if self.head is None:
            raise Exception("no data")

        itr=self.head
        string=""
        while itr:
            
            string += str(itr.data) + "-->"
            itr=itr.next   
        print(string)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count 
    def remove_at(self,index):    
        if index<0 or index >= self.get_length():
            raise Exception("index out of bounds")
        
        if index == 0:
            self.head=self.head.next
            self.head.prev=None
            return

        itr=self.head
        count=0
        while itr:
            if count == index:
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                    break
            itr=itr.next
            count +=1   
    def insert_at(self,index,data)  :
        if index<0 or index >= self.get_length():
            raise Exception("index out of bounds")   
        if index == 0:
            self.insert_at_begining(data)
            return

        itr=self.head
        count=0   
        while itr:
            if count == index:
                itr.prev.next=Node(itr.prev,data,itr)
                # if itr.next:
                #     itr.next.prev=itr.prev
                #     break
            itr=itr.next
            count +=1


if __name__ == '__main__':
    dlist=DLinkedList()
    dlist.insert_at_end(1)
    dlist.insert_at_end(2)
    dlist.insert_at_end(3)
    dlist.printAll()
    print(dlist.get_length())
    dlist.insert_at(3,"data")
    dlist.printAll()