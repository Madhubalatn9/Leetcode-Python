class Graph:
    def __init__(self):
        self.graph={}

    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def AddEdge(self,vertex1,vertex2,isDirect=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirect:
            self.graph[vertex2].append(vertex1)
    def display(self):
        for key,value in self.graph.items():
            print(f"{key} => {value}")
    def getVertex(self):
        for key in self.graph:
            print(key)
    def getEdge(self):
        for key,value in self.graph.items():
            for vertex in value:
             print(f"({key},{vertex})")
    def removeVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for key,value in self.graph.items():
            if vertex in value:
                value.remove(vertex)
    def isEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]
    def removeEdge(self,vertex1,vertex2):
        if self.isEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)


graph=Graph()

graph.AddEdge('A','B')
graph.AddEdge('B','D')
graph.AddEdge('B','C')
graph.AddEdge('C','D')
print("vertices and edges:")
graph.display()
print("Vertices only:")
graph.getVertex()
print("Edges only:")
graph.getEdge()
graph.removeVertex('C')
print("After remove vertices 'c':")
graph.display()

graph.removeEdge('A','B')
print("After remove edges of A and B:")
graph.display()






        