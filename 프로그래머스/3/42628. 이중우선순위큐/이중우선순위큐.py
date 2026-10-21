import heapq
def solution(operations):
    answer = []
    heap=[]
    for i in operations:
        if i[0]=="I":
            heapq.heappush(heap,int(i[2:]))
        elif i=="D -1":
            if len(heap)==0:
                continue
            heapq.heappop(heap)
        else:
            if len(heap)==0:
                continue
            heap.remove(max(heap))
            heapq.heapify(heap)
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), heap[0]]
    return answer