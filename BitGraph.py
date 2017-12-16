class BitGraph:
    def __init__(self,size):
        self.size = size
        self.graph = []


    def getSize(self):
        return self.size

    def generate(self,start,end):
        if end == start:
            return
        else:
            self.graph.append(0)
            return generate(start+1,end)




b = BitGraph(4)
b.generate(0,b.size)
print(b.graph)
