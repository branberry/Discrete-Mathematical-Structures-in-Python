class BitGraph:
    def __init__(self,size):
        self.size = size
        self.graph = []


    def getSize(self):
        return self.size

    def generateGraph(self):
        if self.size <= 0:
            print("graph is too small")





b = BitGraph(0)
b.generateGraph()
