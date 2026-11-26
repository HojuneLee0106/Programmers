from collections import deque
def solution(queue1, queue2):
    answer = -1
    queue1=deque(queue1)
    queue2=deque(queue2)
    s1=sum(queue1)
    s2=sum(queue2)
    c=0
    while c<=(len(queue1)+len(queue2))*2:
        if s1==s2:
            return c
        elif s1<s2:
            x=queue2.popleft()
            s2-=x
            s1+=x
            queue1.append(x)
            c+=1
        else:
            x=queue1.popleft()
            s1-=x
            s2+=x
            queue2.append(x)
            c+=1
    return answer