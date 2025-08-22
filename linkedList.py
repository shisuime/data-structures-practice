class Node:
   def __init__(self,data=None,next=None):
    self.data=data
    self.next=next


class LinkedList:
  def __init__(self):
    self.head=None    
  def insertbegining(self,data):
    node=Node(data,self.head)
    self.head=node

  def insertEnd(self,data):
      if self.head is None:
        self.head=Node(data,None)
        return
      itr=self.head
      while itr.next:
        itr=itr.next
      itr.next=Node(data,None) 

  def printAll(self):
    if self.head is None:
      print("no data")
      return
    itr=self.head
    string=''
    while itr:
      string +=str(itr.data) + "-->"  
      
      itr = itr.next
    print(string)
     
  def insert_values(self,data):
        self.head=None
        for data in data:
          self.insertEnd(data)
  def get_length(self):
    count=0
    itr=self.head
    while itr:
      count +=1
      itr=itr.next
    return count  
  
  def remove_at(self,index):
    itr=self.head
    count=0
    if index < 0 or index >= self.get_length() :
      raise Exception ("out of bounds from either end")

    if index == 0:
      self.head=self.head.next
      return

    while itr:
      if count == index-1:
        itr.next=itr.next.next
        return
      count +=1  
      itr=itr.next  

  def insert_at(self,index,data):
    itr=self.head
    
    if index < 0 or index > self.get_length() :
      raise Exception ("out of bounds from either end")   

    if index==0 :
      self.insertbegining(data)
      return
    count = 0

    while itr:
      if count == index -1:
         itr.next=Node(data,itr.next)
      itr=itr.next
      count +=1    
  def insert_by_value(self,check,data):
    itr=self.head
    if self.head is None:
      raise Exception("no data")  
    
    while itr:
      if itr.data == check:
        itr.next=Node(data,itr.next)
        return
      itr=itr.next
  def remove_by_value(self,data):
    itr=self.head

    if self.head is None:
      raise Exception("no data")
    
    while itr:
      if itr.data == data:
        itr.next=itr.next.next
        return
      itr=itr.next

if __name__ == '__main__':
  linkedList=LinkedList()
  linkedList.insert_values([1,2,3,4,5])
  # linkedList.printAll()
  print(linkedList.get_length())
  # linkedList.remove_at(4)
  linkedList.insert_at(0,"seven")
  linkedList.insert_by_value(1,"eight")
  linkedList.printAll()
  linkedList.remove_by_value("seven")
  linkedList.printAll()


