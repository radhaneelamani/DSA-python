#This code file explains how graphs can be represented in Python
#There are majorly 2 ways: adjacency matrix - nested list; adjacency list - dictionary
""" This file will contain majorly 4 functions along with 1 I/O function:
a. def adjacencyList()
b. def adjacencyMatrix()
c. def weightedAdjacencyList() - weighted graph 
d. def weightedAdjacencyMatrix() - weighted graph
e. def StandardInputOutput()
"""

def adjacencyMatrix(n,m):
    #The size of matrix is (n+1)*(n+1) if indexing is 1 based, if 0 based: n*n
    #indexing can be defined based on the input given
    adjMatrix = [[0 for i in range(0, n+1)] for j in range(0, n+1)]
    print("initialised adjacency matrix:", adjMatrix)
    for i in range(1, m+1):
        #Here u and v are nodes that have an edge
        u,v = map(int, input("Enter edges for adjacency matrix rep: ").split())
        adjMatrix[u][v] = 1
        adjMatrix[v][u] = 1 #This is only for an undirected graph, if the question says directed graph, this is not needed
    
    print("final adjacency matrix showing all the edges:")
    for row in adjMatrix:
        print(row)
    
    """
    Space and Time Complexity:
    Space Complexity: N*N (since we have a matrix of that size)
    Time Complexity:
    1. for storing the graph: O(M)
    2. for printing the matrix row-wise: O(N) - optional
    Disadvantage: Very costly in terms of space, also has a lot of unused space filled with 0's
    """ 
    return adjMatrix

def adjacencyList(n,m):
    #Here our dictionary would be of size N
    #Keys: Nodes, Value: Edges (List)  
    adjList = {}
    for i in range(1, m+1):
        u,v = map(int, input("Enter edges for adjacency list rep: ").split())
        if u in adjList:
            adjList[u].append(v)
        else:
            adjList[u] = [v]
        #If the gaph is directed, exclude the below code
        if v in adjList:
            adjList[v].append(u)
        else:
            adjList[v] = [u]
    print("The adjacency list showing all edges: ", adjList)
    """
    Space and Time Complexity:
    Space Complexity: O(2E) - for every node there are 2 edges for undirected graph
    for directed graph: O(E)
    Time Complexity: O(M) for populating our list
    """
    return adjList

def weightedAdjacencyMatrix(n,m):
    #This is the same as AdjMatrix the only difference is instead of storing 1's at the edge connections we will store its weights
    #The input would be u,v,w: where w is the weight
    weightedAdjMatrix = [[0 for i in range(0, n+1)] for i in range(0, n+1)]
    print("initialised weightedAdjMatrix: ", weightedAdjMatrix)

    for i in range(1, m+1):
        u,v,w = map(int, input("Enter the edges along with their weights for the adjacency matrix: ").split())
        weightedAdjMatrix[u][v] = w
        weightedAdjMatrix[v][u] = w #Again, exclude this line if it is a directed graph
    print("Final weighted adjacency list: ")
    for row in weightedAdjMatrix:
        print(row)
    """
    Space and Time complexity are same as the unweighted approach"""
    return weightedAdjacencyMatrix

def weightedAdjacencyList(n,m):
    #This is the same as AdjList, but instead of simply the numbers in the list, we store a tuple of number and the weight
    weightedAdjList = {}
    for i in range(1, m+1):
        u,v,w = map(int, input("Enter the edges along with weights for the adjacency list: ").split())
        if u in weightedAdjList:
            weightedAdjList[u].append((v,w))
        else:
            weightedAdjList[u] = [(v,w)]
        if v in weightedAdjList:
            weightedAdjList[v].append((u,w))
        else:
            weightedAdjList[v] = [(u,w)]
    print("Final WeightedAdjacency List: ", weightedAdjList)
    return weightedAdjList

def standardInputOutput():
    #It is a standard practice all over that the first line of input is 2 integers n and m
    #here n: number of nodes, m: number of edges
    #then there would be m lines with space separated 2 chars telling us the edge relations
    n,m = map(int, input("Enter number of nodes and edges: ").split())
    return n,m

if __name__ == "__main__":
    n, m = standardInputOutput()
    adjacencyMatrix(n, m)
    adjacencyList(n, m)
    weightedAdjacencyMatrix(n, m)
    weightedAdjacencyList(n, m)



