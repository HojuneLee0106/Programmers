from collections import deque
def solution(n, computers):
    answer = 0
    visited=[-1 for _ in range(n)]
    def connect(x):
        queue=deque()
        queue.append(x)
        while queue:
            l=queue.pop()
            if visited[l]==-1:
                visited[l]=1
                for j in range(n):
                    if j==l:
                        continue
                    if computers[l][j]==1 and visited[j]==-1:
                        queue.append(j)
                    else:
                        continue
            else:
                continue
    for i in range(n):
        if visited[i]==-1:
            connect(i)
            answer+=1
        else:
            continue
    print(visited)
    return answer