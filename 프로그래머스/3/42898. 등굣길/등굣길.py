from collections import deque
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for x, y in puddles:
        dp[y][x] = -1
    def s(x,y):
        hap=0
        if dp[y][x]==-1:
            return -1
        if x-1>0 and dp[y][x-1]!=-1:
            hap+=dp[y][x-1]
        else:
            hap+=0
        if y-1>0 and dp[y-1][x]!=-1:
            hap+=dp[y-1][x]
        else:
            hap+=0
        return hap
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i==1 and j==1:
                continue
            dp[j][i]=s(i,j)
    answer=dp[n][m]%1000000007
    return answer