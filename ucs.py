from queue import PriorityQueue
 
graph = {
    "A":{"B":1,"C":3,"D":7},
    "B":{"D":5},
    "C":{"D":12},
}
 
def UCS(graph, start, end):
    if start == end:
        print("cost is 0")
        return True
    queue = PriorityQueue()
    queue.put((0 , [start]))
    while not queue.empty():
        temp = queue.get()
        if temp[1][-1] == end:
            print("path found",temp[1], "with cost", temp[0])
            return
        child = graph[temp[1][-1]].keys()
        b = []
        for i in temp[1]:
            b.append(i)
        for i in child:
            queue.put((graph[temp[1][-1]][i] + temp[0] , b + [i]))

UCS(graph, "A", "D")
