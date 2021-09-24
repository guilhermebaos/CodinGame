import sys
import math


# Use a function in order to return as soon as we find a link to break!
def bfs():
    si = int(input())

    # Normal BFS stuff
    visited, paths = set([si]), [[si]]
    while True:
        new_paths = []
        for current_path in paths:
            start = current_path[-1]

            next_nodes = [node for node in links_by_index[start] if node not in visited]
            visited.update(set(next_nodes))

            # We do BFS until we find the closest link to a gateway, then, we cut the link
            for node in gateways:
                if node in next_nodes:
                    print(f'{start} {node}')
                    return

            new_paths = [current_path + [node] for node in next_nodes]

        paths = new_paths[:]


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

# Links between nodes
links = [[int(j) for j in input().split()] for _ in range(l)]

# Organize the links
links_by_index = [[i[0] for i in links if i[1] == pos] + [i[1] for i in links if i[0] == pos] for pos in range(n)]

# Indicies of gateway nodes
gateways = [int(input()) for _ in range(e)]


# Game Loop
while True:
    bfs()
