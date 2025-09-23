from collections import deque

def create_graph():
    graph={}
    n=int(input("enter no of nodes : "))
    for i in range(n):
        node=input(f"enter no of nodes {i+1}: ")
        graph[node]=[]
        
    e=int(input(f"enter no of edges (paths): "))
    for j in range(e):
        src=input(f"enter source node for edge {j+1}: ")
        dest=input(f"enter destination node for edge {j+1}: ")
        graph[src].append(dest)
    return graph

def dfs(graph,node,visited = None):
    if visited is None:
        visited=set()
    if node not in visited:
        print(f"visited: {node}")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour,visited)

def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(f"visited : {node}")
            visited.add(node)
            queue.extend(graph[node])

def main():
    print("\n___graph Creation___")
    graph=create_graph()
    print("\n___graph Structure___")
    for node,neighbour in graph.items():
        print(f"{node}->{neighbour}")
    start=input("\n enter starting ode for traversal: ")
    print("\n___dfs Traversal___")
    dfs(graph,start)
    print("\n___bfs Traversal___")
    bfs(graph,start)
if __name__ == "__main__":
    main()
