import heapq
def solution(jobs):
    current=0
    l=len(jobs)
    heapq.heapify(jobs)
    stay=[]
    answer=0
    while True:
        if len(stay)==0 and len(jobs)==0:
            break
        if len(stay)==0:
            s,e=heapq.heappop(jobs)
            answer+=e
            current=s+e
            while True:
                if len(jobs)==0:
                    break
                r,ee=heapq.heappop(jobs)
                if r<=current:
                    heapq.heappush(stay,[ee,r])
                else:
                    heapq.heappush(jobs,[r,ee])
                    break
            print(stay)
        else:
            e,s=heapq.heappop(stay)
            current+=e
            answer+=(current-s)
            while True:
                if len(jobs)==0:
                    break
                r,ee=heapq.heappop(jobs)
                if r<=current:
                    heapq.heappush(stay,[ee,r])
                else:
                    heapq.heappush(jobs,[r,ee])
                    break        
    return answer//l