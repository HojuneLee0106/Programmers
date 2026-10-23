def solution(n, times):
    left=0
    right=max(times)*n
    answer=0
    while left<=right:
        mid=(right+left)//2
        people=sum(mid//time for time in times)
        if people>=n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
        
    return answer