def solution(n):
    answer = [[]]
    def tower(start, mid, end, N):
        if N==1:
            return [[start, end]]
        return tower(start, end, mid,N-1) + [[start, end]]+ tower(mid, start, end,N-1)
    
    return tower(1,2,3,n)