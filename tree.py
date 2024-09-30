# class TreeNode:
#     def __init__(self,data,designation):
#         self.data=data
#         self.children=[] 
#         self.parent =None
#         self.designation=designation


#     def addChild(self,child):
#         child.parent=self
#         self.children.append(child)

#     def printTree(self,type="name"):
#         space= " " * self.getLevel() * 3
#         prefix=space+"|--" if self.parent else ""
#         if type == "name":
#             print(prefix+ self.data )
#         elif type == "designation":
#             print(prefix+f"({self.designation})" )   
#         else:

#             print(prefix + self.data +f"({self.designation})" )
#         if self.children:
#             for child in self.children:
#                 child.printTree(type)
#     def getLevel(self):
#         p=self.parent
#         level=0
#         while p is not None:
#             level +=1
#             p=p.parent
#         return level
# def projectTree():
#     root=TreeNode("N","CEO")


#     laptop=TreeNode("L","CTO")
#     laptop.addChild(TreeNode("h","IH"))
#     laptop.addChild(TreeNode("d","CM"))
#     laptop.addChild(TreeNode("lenovo","AM"))
#     root.addChild(laptop)

#     tv=TreeNode("TV","HR")
#     tv.addChild(TreeNode("andriod","RM"))
#     tv.addChild(TreeNode("normal","PM"))
#     root.addChild(tv)

#     # phone=TreeNode("Cellphone")
#     # phone.addChild(TreeNode("lava"))
#     # phone.addChild(TreeNode("iphone"))
#     # root.addChild(phone)

#     # print(tv.getLevel())

#     return root


# root=projectTree()
# root.printTree("both")

# class TreeNode:
#     def __init__(self,data,):
#         self.data=data
#         self.children=[] 
#         self.parent =None
        


#     def addChild(self,child):
#         child.parent=self
#         self.children.append(child)

#     def printTree(self,level):
#         if self.getLevel() > level:
#             return

#         space= " " * self.getLevel() * 3
#         prefix=space+"|--" if self.parent else ""
       
#         print(prefix + self.data )
#         if self.children:
#             for child in self.children:
#                 child.printTree(level)
#     def getLevel(self):
#         p=self.parent
#         level=0
#         while p is not None:
#             level +=1
#             p=p.parent
#         return level
# def projectTree():
#     root = TreeNode("Global")

#     india = TreeNode("India")

#     gujarat = TreeNode("Gujarat")
#     gujarat.addChild(TreeNode("Ahmedabad"))
#     gujarat.addChild(TreeNode("Baroda"))

#     karnataka = TreeNode("Karnataka")
#     karnataka.addChild(TreeNode("Bangluru"))
#     karnataka.addChild(TreeNode("Mysore"))

#     india.addChild(gujarat)
#     india.addChild(karnataka)

#     usa = TreeNode("USA")

#     nj = TreeNode("New Jersey")
#     nj.addChild(TreeNode("Princeton"))
#     nj.addChild(TreeNode("Trenton"))

#     california = TreeNode("California")
#     california.addChild(TreeNode("San Francisco"))
#     california.addChild(TreeNode("Mountain View"))
#     california.addChild(TreeNode("Palo Alto"))

#     usa.addChild(nj)
#     usa.addChild(california)

#     root.addChild(india)
#     root.addChild(usa)

#     return root
    

    

   


# root=projectTree()
# root.printTree(3)


# lidwa=[1,2,3,4]
# print(enumerate(lidwa))