def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    check=[]
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            check.append(i)
    for i in check:
        lost.remove(i)
    answer = n - len(lost)
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            answer += 1
        elif l + 1 in reserve: 
            reserve.remove(l + 1)
            answer += 1
            
    return answer