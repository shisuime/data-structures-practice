class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
        
class DLinkedList:

    def __init__(self):
        self.head=None

    def print(self):
       if self.head is None:
           print("no data available")
           return
       itr=self.head
       lstr=''
       while itr:
           lstr +=str(itr.data) + '-->'
           itr=itr.next
       print(lstr)    


    def insert_at_beginning(self,data):
       node=Node(None,data,self.head)

       if self.head is not None:
           self.head.prev=node

       self.head=node    
   

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(None,data,None)
            return 

        itr=self.head
        while itr.next:
            itr=itr.next

        node=Node(itr,data,None)
        itr.next=node       
             


    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def getLength(self):
       if self.head is None:
           raise Exception("no data found")
       count=0
       itr=self.head
       while itr:
           count +=1
           itr=itr.next

       return count    
    
    def remove_at(self,index):
        if index < 0 or index >= self.getLength():
           raise Exception("index out of bounds")
        
        if index == 0:
            self.head=self.head.next
            if self.head:

                self.head.prev=None
            return
        
        count=0
        itr=self.head
        while itr:
            if count == index:
               itr.prev.next=itr.next
               if itr.next:
                   itr.next.prev=itr.prev
               return    
            count +=1
            itr=itr.next

    def insert_at(self,index,data):
       if index < 0 or index > self.getLength():
           raise Exception("index out of bounds")
       
       if index == 0:
           node=Node(None,data,self.head)
           if self.head:
               self.head.prev=node
           self.head=node
           return    

       count=0
       itr=self.head
       while itr:
           if count == index -1:
               node=Node(itr,data,itr.next)
               if itr.next:
                   itr.next.prev=node
               itr.next=node
               return    
           count +=1
           itr=itr.next


    def insert_after_value(self,data_after,data_to_insert):
       if self.head is None:
           raise Exception("no data available")
       
       itr=self.head
       while itr:
           if itr.data == data_after:
               node=Node(itr,data_to_insert,itr.next)
               if itr.next:
                   itr.next.prev=node
               itr.next=node
               return
           itr=itr.next
        
       raise Exception("value not found")
    def remove_by_value(self,data_to_remove):
        if self.head is None:
           raise Exception("no data available")
        
        itr=self.head
        while itr:
            if itr.data == data_to_remove:

                if itr.prev is None:
                    self.head=itr.next
                    if self.head:
                        self.head.prev=None
                    return
                    

                if itr.next:
                    itr.next.prev=itr.prev
                itr.prev.next=itr.next
                return
            itr=itr.next

        raise Exception("value not found")     

    def print_backward(self):
       
       if self.head is None:
           print("no data available")
           return
       
       itr=self.head
       
       while itr.next:
           itr=itr.next
          
       lstr=''
       while itr:
           lstr +=str(itr.data) + '-->'
           itr=itr.prev
       print(lstr)    
        
        

if __name__ == '__main__':
    ll=DLinkedList()
    # ll.insert_at_beginning(1)
    # ll.insert_at_beginning(2)
    # ll.insert_at_beginning(3)
    # ll.insert_at_beginning(4)
    # ll.insert_at_end(0)
    ll.insert_values([1,2,3,4,5,6,67])
    # ll.remove_at(7)
    # ll.insert_at(1,432)
    # ll.insert_after_value(0,74)
    # ll.remove_by_value(67)
    # ll.print()
    ll.print_backward()
