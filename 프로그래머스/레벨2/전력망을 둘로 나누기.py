#(1,8), (1,8), (3,6), (1,8), (1,8), (6,3), (8,1), (8,1)
def solution(n, wires):
    answer = []
    for idx, i in enumerate(wires,start=1):
        if idx == len(wires):
            break
        graph_a = make_graph(wires[:idx-1],n)     
        graph_b = make_graph(wires[idx:],n)
        final_a = bfs([], graph_a, wires[idx-1][0])
        final_b = bfs([], graph_b, wires[idx-1][1])
        answer.append(abs(final_a - final_b))
    return min(answer)
    
def make_graph(wire,n):
    graph = dict()
    for i in wire:
        if(i[0] not in graph):
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]] = graph.get(i[0]) + [i[1]]
    for i in range(1,n+1):
        if(i not in graph):
            graph[i] = []
            
    for i in wire:
        if(i[1] not in graph):
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]] = graph.get(i[1]) + [i[0]]
    return graph

def bfs(visited, graph, node):
    queue=[]
    final = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        final.append(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return len(final)