#Graph_algorithms.py

"""
In this script we implement 4 graph algorithms,dfs,bfs,prim and kruskal
"""

import heapq

from collections import deque


def dfs(graph, start, visited=None):

    """
    depth first seach
    """

    if visited is None:

        visited = set()
    
    visited.add(start)

    result = [start]
    
    for neighbor in graph[start]:

        if neighbor not in visited:

            result.extend(dfs(graph, neighbor, visited))
            
    return result


def bfs(graph, start):

    """
    breadth first search
    """

    visited = set([start])

    queue = deque([start])

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)
        
        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)
                
    return result


def prim(graph, start):

    """
    prim's minimum spanning tree
    """
    mst = []

    visited = set([start])

    edges = [(weight, start, to) for to, weight in graph[start].items()]

    heapq.heapify(edges)

    total_cost = 0

    while edges:

        weight, frm, to = heapq.heappop(edges)
        
        if to not in visited:

            visited.add(to)

            mst.append((frm, to, weight))

            total_cost += weight
    
            for next_to, next_weight in graph[to].items():

                if next_to not in visited:

                    heapq.heappush(edges, (next_weight, to, next_to))

    return mst, total_cost


class unionfind:

    """disjoint Set  to detect cycles in Kruskal's Algorithm"""

    def __init__(self, vertices):

        self.parent = {v: v for v in vertices}

        self.rank = {v: 0 for v in vertices}

    def find(self, item):

        if self.parent[item] != item:

            self.parent[item] = self.find(self.parent[item])

        return self.parent[item]

    def union(self, x, y):

        xroot = self.find(x)

        yroot = self.find(y)
        
        if xroot == yroot:

            return False 
            
        if self.rank[xroot] < self.rank[yroot]:

            self.parent[xroot] = yroot

        elif self.rank[xroot] > self.rank[yroot]:

            self.parent[yroot] = xroot

        else:

            self.parent[yroot] = xroot

            self.rank[xroot] += 1

        return True


def kruskal(graph):

    """
    Kruskal's minimum spanning tree algorithm
    """

    mst = []

    edges = []

    seen_edges = set()
    
    for u in graph:

        for v, weight in graph[u].items():

            if (v, u) not in seen_edges:

                edges.append((weight, u, v))

                seen_edges.add((u, v))

    edges.sort()

    uf = unionfind(graph.keys())

    total_cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))

            total_cost += weight

    return mst, total_cost



if __name__ == "__main__":
    
  
    example_graph = {

        "a" : {"b" : 4, "c" : 2},

        "b" : {"a" : 4, "c" : 1, "d" : 5},

        "c" : {"a" : 2, "b" : 1, "d" : 8, "e" : 10},

        "d" : {"b" : 5, "c" : 8, "e" : 2, "f" : 6},

        "e" : {"c" : 10, "d" : 2, "f" : 3},

        "f" : {"d" : 6, "e" : 3}

    }

    start_node = 'a'

    
    #Dfs
    dfs_result = dfs(example_graph, start_node)

    print(f"dfs starting from '{start_node}':")

    print(dfs_result)

    #Bfs
    bfs_result = bfs(example_graph, start_node)

    print(f"bfs starting from '{start_node}':")

    print(bfs_result)
    
    # 3. Prim's Algorithm
    prim_mst, prim_cost = prim(example_graph, start_node)

    print(f"prim's algorithm starting from '{start_node}':")

    for u, v, w in prim_mst:

        print(f"  edge: {u} - {v} (weight: {w})")

    print(f" total mst cost : {prim_cost}")

    # 4. Kruskal's Algorithm
    kruskal_mst, kruskal_cost = kruskal(example_graph)

    print("kruskal's algorithm")

    for u, v, w in kruskal_mst:

        print(f"  edge: {u} - {v} (weight: {w})")

    print(f" total mst cost: {kruskal_cost}")