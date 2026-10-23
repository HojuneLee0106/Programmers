import heapq
def solution(N, road, K):
    graph={i:[]for i in range(1,N+1)}
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
    print(graph)
    distance={i:float("inf") for i in range(1,N+1)}
    distance[1]=0
    heap=[(0,1)]
    while heap:
        d,town=heapq.heappop(heap)
        if distance[town]<d:
            continue
        for next_node, dis in graph[town]:
            if dis+d<distance[next_node]:
                distance[next_node]=dis+d
                heapq.heappush(heap,(dis+d,next_node))
        
    return sum(1 for dist in distance.values() if dist<=K)
