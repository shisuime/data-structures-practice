
# class Animal:
#     def sound(self):
#         return "some sound"
    

# class Dog(Animal):
#     def sound(self):
#         self.a=5
#         return ("Bark",self.a)

# class Cat(Animal):
#     def sound(self,cheing):
#         cheing.b=7
#         return ("meow",cheing.b )       
    

# dog=Dog()
# cat=Cat()
# animal=Animal()

# print(dog.sound())
# print(cat.sound({}))
# print(animal.sound())
# print(animal)

# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def enginestart(self):
#         pass

# class Car(Vehicle):
#     def __init__(self,brand):
#         self.brand=brand  
#     def enginestart(self):
#         print(f"{self.brand} engine started")      

# obj=Car("toyota")
# obj.enginestart()        

# i=0
# for i in range(100, 501):
#     if (i % 11 == 0) and (i % 3 != 0):
#         print(i)
    
        
# studentMarks=int(input("enter marks"))

# if(studentMarks>60 and studentMarks < 100):
#     print("passed")
# else:
#     print("error")

from collections import deque

stack=deque()
stack.append("hi")
stack.append("dwa")
stack.append("hdwadwai")