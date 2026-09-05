from collections import deque
def solution(maps):
    answer = []
    maps = [list(row) for row in maps]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            c=0
            if maps[i][j]!="X":
                queue=deque()
                queue.appendleft((i,j))
                while queue:
                    y,x=queue.popleft()
                    if x<0 or y<0 or y>=len(maps) or x>=len(maps[0]):
                        continue
                    if maps[y][x]=="X":
                        continue
                    c+=int(maps[y][x])
                    maps[y][x]="X"
                    queue.append((y,x+1))
                    queue.append((y,x-1))
                    queue.append((y+1,x))
                    queue.append((y-1,x))
                if c>=0:
                    answer.append(c)
    answer.sort()
    if len(answer)==0:
        return [-1]
    else:
        return answer