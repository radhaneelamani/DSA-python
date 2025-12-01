#Breadth First Search Technique - Traversal
#Usually graphs are of 2 types: 0-based indexing and 1-based indexing
#also called level wise traversal
#given starting node, all of the nodes in the graph have to be listed out based on their levels
"""
Example graph:
            1              #Level 0
        2       6          #Level 1
    3      4  7     8      #Level 2
             5             #Level 3
The traversal of this graph, BFS: 
Case: when the starting node is 1
1 -> 2 -> 6 -> 3 -> 4 -> 7 -> 8 -> 5
(level 0 -> level 1 -> level 2 -> level 3) 

Case: when the starting node is 6
6 -> 1 -> 7 -> 8 -> 2 -> 5 -> 3 -> 4
( [6: level 0], at 1 lenght distance [1,7,8: level 1]
  [2,5: level 2], [3,4: level 3])
"""
#We use a queue data structure here: FIFO
#Initially we will have 2 data structs: (i) Queue, (ii) Visited Array
#the first element in the queue would be the starting node
#The visited array would be of size (n+1) when it is 1-based indexing
#In the visited array, we mark the starting node as 1 and the rest all as 0 initially, then as an d when we push elements into the queue we mark them as 1
#We pop from the queue until it is empty and print it, the element that we are popping we will add its edges elements into the queue checking from the adj list

from GraphRepresentations import standardInputOutput, adjacencyList
#from collections import deque "can be used if collections are allowed"


def bfs(startingNode, n, m, adjList):
    print("Starting breadth first search from: ", startingNode)

    visitedArray = [0 for i in range(n+1)] #Assuming a 1-based indexing
    print("Initialised visited array: ", visitedArray)
    queue = []
    #queue = deque()
    bfs = []

    visitedArray[startingNode] = 1
    print("marking starting node as visited: ", visitedArray)
    queue.append(startingNode)
    print("adding starting node into queue: ", queue)

    while queue:
        print("checking if the queue is not empty")
        node = queue.pop(0)
        #node = queue.popleft()
        print("currently at: ", node)
        bfs.append(node)
        
        for i in adjList[node]:
            if visitedArray[i] == 0:
                print("checking if the node's neighbours have been already visited")
                print("adding the node's neighbour to the visited array: ", i)
                visitedArray[i] = 1
                queue.append(i)
    
    return bfs


if __name__ == "__main__":
    startingNode = int(input("Enter your starting node: "))
    n,m = standardInputOutput()
    adjList = adjacencyList(n, m)
    print(bfs(startingNode, n, m, adjList))


"""
Space Complexity:
3 data structures: 1 queue, 1 visited array, 1 bfs: O(N)
Time Complexity:
node goes once into the BFS - runs on all its degrees:
O(N) + O(2E)
"""

