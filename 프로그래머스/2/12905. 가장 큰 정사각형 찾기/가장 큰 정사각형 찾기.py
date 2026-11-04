def solution(board):
    answer = 0
    dp=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                dp[i][j]=0
            else:
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    if dp[i-1][j]==dp[i][j-1] and dp[i][j-1]==dp[i-1][j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            answer=max(dp[i][j]**2,answer)
    return answer