from queue import PriorityQueue
from graph import graph,h

def astar(start,target):
    if start==target:
        print("Cost is 0")
        return True
    q=PriorityQueue()
    q.put((0+h[start],[start]))
    while q.empty()==False:
        temp=q.get()
        print(temp)
        if temp[1][len(temp[1])-1]==target:
            print(temp[1],"path found"," of distance",temp[0])
            return
             
        childKeys=graph[temp[1][len(temp[1])-1]].keys()
        b=[]
        for i in temp[1]:
            b.append(i)
        a=h[temp[1][-1]]
        for i in childKeys:
            q.put((graph[temp[1][len(temp[1])-1]][i]+temp[0]+h[i]-a,b+[i]))


            
astar("Arad","Bucharest")
