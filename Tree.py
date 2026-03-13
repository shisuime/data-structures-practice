class Tree:
    def __init__(self,data,designation=None):
        self.data=data
        self.children=[]
        self.parent=None
        self.designation=designation

    def addChild(self,child):

        child.parent=self
        self.children.append(child)  


    def getLevel(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent

        return level    


    def printTree(self,type):
        spaces=" " * self.getLevel() * 3

        prefix=spaces + "|__" if self.parent else ""


        if type == "name":
            value=self.data
        elif type == "designation":
            value=self.designation
        elif type == "both":
            value=f"{self.data} ({self.designation})"    

        else:
            value=self.data


        print(prefix + value)
        if self.children:
            for child in self.children:
                child.printTree(type)
            

def build_product_tree():
    electronics=Tree("Electroncis")

    laptops=Tree("Laptop")
    laptops.addChild(Tree("Lenovo"))
    laptops.addChild(Tree("Dell"))
    laptops.addChild(Tree("Hp"))

    smartPhones=Tree("Smartphones")
    smartPhones.addChild(Tree("Samsung"))
    smartPhones.addChild(Tree("Apple"))
    smartPhones.addChild(Tree("Blackberry"))

    tv=Tree("TV")
    tv.addChild(Tree("LG"))
    tv.addChild(Tree("Sony"))
    tv.addChild(Tree("BenQ"))

    electronics.addChild(laptops)
    electronics.addChild(smartPhones)
    electronics.addChild(tv)

    return electronics


def build_management_tree():
    # CTO Hierarchy
    infra_head = Tree("Vishwa","Infrastructure Head")
    infra_head.addChild(Tree("Dhaval","Cloud Manager"))
    infra_head.addChild(Tree("Abhijit", "App Manager"))

    cto = Tree("Chinmay", "CTO")
    cto.addChild(infra_head)
    cto.addChild(Tree("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = Tree("Gels","HR Head")

    hr_head.addChild(Tree("Peter","Recruitment Manager"))
    hr_head.addChild(Tree("Waqas", "Policy Manager"))

    ceo = Tree("Nilupul", "CEO")
    ceo.addChild(cto)
    ceo.addChild(hr_head)

    return ceo

if __name__ == '__main__':
    result=build_management_tree()

    # print(result.getLevel())

    result.printTree("name")
    result.printTree("designation")
    result.printTree("both")


           