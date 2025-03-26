import networkx as nx
import graph as g

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]
G = g.create_graph(edges)

print("--- Graph Information ---")
print(f"Nodes: {list(G.nodes)}")
print(f"Edges: {list(G.edges)}")

node = 2
degree = g.get_degree(G, node)
print(f"Degree of node {node}: {degree}")

start_node = 1
dfs_result = g.dfs_traversal(G, start_node)
bfs_result = g.bfs_traversal(G, start_node)
print(f"DFS Traversal from {start_node}: {dfs_result}")
print(f"BFS Traversal from {start_node}: {bfs_result}")

source, target = 1, 4
shortest_path = g.find_shortest_path(G, source, target)
print(f"Shortest path from {source} to {target}: {shortest_path}")

print("--- Visualizing Graph ---")
g.visualize_graph(G)
