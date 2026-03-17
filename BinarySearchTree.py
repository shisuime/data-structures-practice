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



def buildTree(elements):
    root=BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])

    return root    


if __name__ == "__main__":
    numbers=[17,4,1,6,34,68,8,17,6]

    numbers_tree=buildTree(numbers)

    # print(numbers_tree.inOrderTraversal())
    print(numbers_tree.search(1545))


