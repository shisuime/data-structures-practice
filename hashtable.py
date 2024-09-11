import pandas as pd
# day=("a","b","c")
# price=[1,2,3]
# stock_prices={}
# for d,p in zip(day,price):
#     stock_prices[d]=p


# print(stock_prices)

# def __getitem__(self,key):
#         h=self.get_hash(key)

#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
        

#     def __setitem__(self,key,val):
#         h=self.get_hash(key)
#         found=False
#         for idx,element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0]==key:
#                 self.arr[h][idx]=(key,val)
#                 found=True
#                 break

#         if not found:
#             self.arr[h].append((key,val))

#     def __delitem__(self,key):
#         h=self.get_hash(key)
#         for index,element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][index]



# t=HashTable()
# t["march 6"]=16
# t["march 17"]=18

# print(t["march 6"])
# # print(t.arr)
# print(t["march 17"])
# del t["march 17"]
# del t["march 6"]
# print(t.arr)
# print(t["march 17"])

#hashfunction
# def get_hash(key):
#     h=0
#     for char in key:
#         h +=ord(char)
#     return h % 100

# print(get_hash("march 22"))



# class HashTable:
#     def __init__(self) :
#         self.MAX=10
#         self.arr=[[] for i in range(self.MAX)]

#     def get_hash(self,key):
#         h=0
#         for char in key:
#             h +=ord(char)
#         return h % self.MAX
    
#     def __setitem__(self,key,value):
#         h=self.get_hash(key)
#         found=False

#         for index,element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0]==key:
#                 self.arr[h][index]=(key,value)
#                 found=True
#                 break

#         if not found:
#             self.arr[h].append((key,value))     

#     def __getitem__(self,key):
#         h=self.get_hash(key)

#         for  element in enumerate(self.arr[h]):
#              element[0]==key
#              return element[1]

#     def __delitem__(self,key):
#             h=self.get_hash(key)

#             for index,element in enumerate(self.arr[h]):
#                 element[0]==key
#                 del self.arr[h][index]

#     def averageCount(self,data):
#         # print(data[1])
#         # i=0
#         # res=0
#         # while i<7:
#         #   res=res+data[i]
#         #   i=i+1
#         # print("total",res/7)
#         print("average",sum(data[0:7])/7)
           

#     def maxTemp(self,data):
#         # max=0
#         # for elements in data:        
#         #     if max < elements :
#         #         max=elements
            
#         # print("max temp",max)
#         print(max(data),"max")

# obj= HashTable()
# file_path="nyc_weather.csv"
# df=pd.read_csv(file_path)
# # print(df["temperature(F)"][1])
# obj.averageCount(df["temperature(F)"])
# obj.maxTemp(df["temperature(F)"])

# word_count={}

# with open("poem.txt","r") as f:
#     for line in f:
#         tokens=line.split(" ")
#         for token in tokens:
#             token=token.replace("\n","")
#             if token in word_count:
#                 word_count[token] +=1
#             else:
#                 word_count[token]=1    


# print(word_count)

#Stack

# from collections import deque
# class Stack:
#     def __init__(self):
#         self.container=deque()

#     def push (self,value):
#         return self.container.append(value)    

#     def pop (self):
#         return self.container.pop()

#     def size(self):
#         return len(self.container)

# def reverse_string(string):
#         obj=Stack()

#         for character in string:
#             obj.push(character)


#         revereseString=""
#         while obj.size() !=0:
#             revereseString +=obj.pop()


#         return revereseString          

# print(reverse_string("we will conquere covid-19"))

# from collections import deque
# class Stack:
#     def __init__(self):
#         self.container=deque()

#     def push (self,value):
#         return self.container.append(value)    

#     def pop (self):
#         return self.container.pop()

#     def size(self):
#         return len(self.container)

# def is_match(ch1,ch2):
#       match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#       return match_dict[ch1]==ch2

# def isBalanced(string):
#     stack=Stack()

#     for ch in string:
#         if ch =="(" or ch =="[" or ch =="{":
#             stack.push(ch)
#         if ch ==")" or ch =="]" or ch =="}": 
#             if stack.size()==0:
#                 return False
#             if not is_match(ch,stack.pop()):
#                 return False  

#     return stack.size()==0

# print(isBalanced("({a+b})"))
# print(isBalanced("))((a+b}{"))
# print(isBalanced("((a+b))"))
# print(isBalanced("((a+g))"))
# print(isBalanced("))"))
# print(isBalanced("[a+b]*(x+2y)*{gg+kk}"))

#queue


# queue=[]
# queue.insert(0,2)
# queue.insert(0,2213)
# queue.insert(0,32132)
# print(queue)

# queue.pop()
# queue.pop()
# print(queue)

from collections import deque
q=deque()
q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)
q.appendleft(5)
q.pop()
print(q)

