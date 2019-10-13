from collections import deque

graph = dict()
graph['A'] = ['B', 'C', 'D']
graph['B'] = ['A', 'C']
graph['C'] = ['B', 'D']
graph['D'] = ['C', 'A']


def process(node):
    print(node)


def breadth_first_search(graph, root):
    q = deque(root)
    # has_been_in_the_q has 2 kinds of data
    # 1. The node has been processed
    # 2. The node has not been processed but it is already in the queue.
    has_been_in_the_q = []

    while len(q) > 0:
        node = q.popleft()
        process(node)
        has_been_in_the_q.append(node)

        adj_nodes = graph[node]
        for n in adj_nodes:
            if n in has_been_in_the_q:
                continue
            q.append(n)
            has_been_in_the_q.append(n)


breadth_first_search(graph, 'A')