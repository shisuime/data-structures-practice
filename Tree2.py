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


    def printTree(self,level):
        if self.getLevel() > level:
            return

        spaces=" " * self.getLevel() * 3

        prefix=spaces + "|__" if self.parent else ""

        value=self.data


        print(prefix + value)
        if self.children:
            for child in self.children:
                child.printTree(level)
            

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


def build_location_tree():
    root = Tree("Global")

    india = Tree("India")

    gujarat = Tree("Gujarat")
    gujarat.addChild(Tree("Ahmedabad"))
    gujarat.addChild(Tree("Baroda"))

    karnataka = Tree("Karnataka")
    karnataka.addChild(Tree("Bangluru"))
    karnataka.addChild(Tree("Mysore"))

    india.addChild(gujarat)
    india.addChild(karnataka)

    usa = Tree("USA")

    nj = Tree("New Jersey")
    nj.addChild(Tree("Princeton"))
    nj.addChild(Tree("Trenton"))

    california = Tree("California")
    california.addChild(Tree("San Francisco"))
    california.addChild(Tree("Mountain View"))
    california.addChild(Tree("Palo Alto"))

    usa.addChild(nj)
    usa.addChild(california)

    root.addChild(india)
    root.addChild(usa)

    return root

if __name__ == '__main__':
    result=build_location_tree()

    # print(result.getLevel())

    result.printTree(3)


           