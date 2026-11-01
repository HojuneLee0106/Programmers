def solution(n):
    answer = 0
    if n <= 2:
        return n
    mem=[0 for _ in range(n+1)]
    mem[1]=1
    mem[2]=2
    for i in range(3,n+1):
        mem[i]=mem[i-1]+mem[i-2]
    answer=mem[n]%1234567
    return answer