def solution(sequence, k):
    answer = [0, len(sequence)]
    left=0
    s=0
    for right in range(len(sequence)):
        s+=sequence[right]
        while s>k:
            s-=sequence[left]
            left+=1
        if s==k and right-left<answer[1]-answer[0]:
            answer=[left,right]
    return answer