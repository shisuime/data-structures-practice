# day=("a","b","c")
# price=[1,2,3]
# stock_prices={}
# for d,p in zip(day,price):
#     stock_prices[d]=p


# print(stock_prices)

#hashfunction
# def get_hash(key):
#     h=0
#     for char in key:
#         h +=ord(char)
#     return h % 100

# print(get_hash("march 22"))

class HashTable:
    def __init__(self) :
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:
            h +=ord(char)
        return h % self.MAX

    def add(self,key,val):
        h=self.get_hash(key)   
        self.arr[h]=val

    def get(self,key):
        h=self.get_hash(key)
        return self.arr[h]     

t=HashTable()
t.add("march6",1120)
var=t.get("march6")     
print(t.arr)