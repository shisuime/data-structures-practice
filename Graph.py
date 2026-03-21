class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graphDict={}

        for start,end in self.edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start]=[end]
        print(self.graphDict,"graph dict")

    def getPath(self,start,end,path=[]):
        path= path + [start]
        if start == end:
            return [path]   

        if start not in self.graphDict:
            return []  
        paths=[]
        for node in self.graphDict[start]:
            if node not in path:
                new_paths=self.getPath(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths    

    def getShortestPath(self,start,end,path=[]):
        path=path + [start]
        
        if start == end:
            return path

        if start not in self.graphDict:
            return None

        shortestPath=None
        for node in self.graphDict[start]:
            if node not in path:
                sp=self.getShortestPath(node,end,path)
                if sp:
                    if shortestPath is None or len(sp) < len(shortestPath):
                        shortestPath=sp

        return shortestPath                



if __name__ == "__main__":
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    ]

    start="Mumbai"
    end="Dubai"

    route_graph=Graph(routes)
    # answer= route_graph.getPath(start,end)
    answer= route_graph.getShortestPath(start,end)
    # print(f"path between {start} and {end} is :",answer)
    print(f"shortest path between {start} and {end} is :",answer)

