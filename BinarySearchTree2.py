class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def addChild(self,data):
        if self.data == data:
            return
        
        if data < self.data:
            
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinarySearchTree(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinarySearchTree(data)    
            
    def inOrderTraversal(self):
        elements=[]

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements    

    def search(self,value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                 return self.left.search(value)
            else:
                return False

        if value > self.data:
            if self.right:
               return self.right.search(value)
            else:
                return False  

    def findMin(self):
        if self.left is None:
            return self.data
        return self.left.findMin() 
    def findMax(self):
        if self.right is None:
            return self.data
        return self.right.findMax()   

    def calcSum(self):
        # total = left sum + middle + right sum   
        totalLeft=self.left.calcSum() if self.left else 0  
        totalRight=self.right.calcSum() if self.right else 0  
        return totalLeft + self.data + totalRight  

    def postOrderTraversal(self):
        elements=[]

        if self.left:
            elements += self.left.postOrderTraversal()

        if self.right:
            elements += self.right.postOrderTraversal()

        elements.append(self.data)   
        return elements    

    def preOrderTraversal(self):
        elements=[]

        elements.append(self.data)  

        if self.left:
            elements += self.left.preOrderTraversal()

        if self.right:
            elements += self.right.preOrderTraversal()

         
        return elements  

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_value = self.right.findMin()
            self.data = min_value
            self.right = self.right.delete(min_value)

        return self
    

    def delete2(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            max_value = self.left.findMax()
            self.data = max_value
            self.left = self.left.delet2(max_value)

        return self
        



def buildTree(elements):
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root    


if __name__ == "__main__":
    numbers=[17,4,2,6,34,8,17,6,20]

    numbers_tree=buildTree(numbers)

    # print(numbers_tree.inOrderTraversal())
    # print(numbers_tree.search(1545))
    # print(numbers_tree.findMin())
    # print(numbers_tree.findMax())
    # print(numbers_tree.calcSum())
    # print(numbers_tree.postOrderTraversal())
    # print(numbers_tree.preOrderTraversal())
    numbers_tree.delete2(34)
    print(numbers_tree.preOrderTraversal())



