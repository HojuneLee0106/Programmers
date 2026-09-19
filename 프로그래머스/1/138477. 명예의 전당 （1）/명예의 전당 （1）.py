import heapq
def solution(k, score):
    answer = []
    heap=[]
    for i in range(len(score)):
        heapq.heappush(heap,score[i])
        if len(heap)>k:
            heapq.heappop(heap)
        answer.append(heap[0])
    return answer