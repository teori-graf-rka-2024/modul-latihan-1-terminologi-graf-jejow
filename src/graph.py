import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from typing import List, Tuple

def create_graph(edges: List[Tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree(node)

def dfs_traversal(G: nx.Graph, start: int) -> List[int]:
    visited = []

    def dfs(node: int):
        if node not in visited:
            visited.append(node)
            for neighbor in G.neighbors(node):
                dfs(neighbor)
                
    dfs(start)
    return visited

def bfs_traversal(G: nx.Graph, start: int) -> List[int]:
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in G.neighbors(node):
                queue.append(neighbor)
    return visited

def find_shortest_path(G: nx.Graph, source: int, target: int) -> List[int]:
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return []  # Mengembalikan list kosong jika tidak ada jalur

def visualize_graph(G: nx.Graph) -> None:
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
    plt.savefig("graph_visualization.png")
    plt.show()
