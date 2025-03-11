import networkx as nx
import matplotlib.pyplot as plt
import time

def draw_graph_step(graph, pos, added_edges, step):
    plt.clf()
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
    nx.draw_networkx_edges(graph, pos, edgelist=added_edges, edge_color='red', width=2)
    plt.title(f"Spanning Tree Construction - Step {step}")
    plt.pause(1)

def construct_spanning_tree(adj_list, order):
    graph = nx.Graph()
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)
    
    pos = nx.spring_layout(graph)  # positioning for visualization
    
    plt.figure()
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
    plt.title("Original Graph")
    plt.show()
    
    spanning_tree = nx.Graph()
    spanning_tree.add_nodes_from(adj_list.keys())
    
    visited = set()
    added_edges = []
    stack = [order[0]]
    visited.add(order[0])
    order_index = {node: i for i, node in enumerate(order)}
    
    step = 1
    while stack:
        node = stack[-1]
        unvisited_neighbors = [n for n in adj_list[node] if n not in visited]
        
        if unvisited_neighbors:
            unvisited_neighbors.sort(key=lambda x: order_index[x])
            neighbor = unvisited_neighbors[0]
            visited.add(neighbor)
            stack.append(neighbor)
            spanning_tree.add_edge(node, neighbor)
            added_edges.append((node, neighbor))
            draw_graph_step(spanning_tree, pos, added_edges, step)
            step += 1
        else:
            stack.pop()
    
    plt.show()

if __name__ == "__main__":
    
    # Section 9.3, Exercise 6
    adj_list = {
        'a': ['b', 'g', 'c'],
        'b': ['d', 'a', 'g'],
        'c': ['d', 'e', 'a'],
        'd': ['c', 'f', 'b'],
        'e': ['g', 'c', 'f'],
        'f': ['d', 'e', 'h'],
        'g': ['e', 'a', 'b'],
        'h': ['f']
    }
    order = ['h', 'f', 'd', 'b', 'g', 'e', 'c', 'a']  # dfs order
    
    construct_spanning_tree(adj_list, order)
