graph = []
def generate(start,end,previousbit):
    if start == end:
        return
    else:
        graph.insert(start,'0000')
        return generate(start+1,end,previousbit)

generate(0,4,0)
print(graph)