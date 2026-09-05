def solution(N, stages):
    answer = []
    class Stage:
        def __init__(self, diff, challenge, success, ratio):
            self.diff=diff
            self.challenge=challenge
            self.success=success
            self.ratio=ratio
    game={}
    max_s=max(stages)
    for i in range(1,N+1):
        game[i]=Stage(i,0,0,0)
    for i in range(len(stages)):
        player_stage=stages[i]
        for j in range(1,player_stage+1):
            if j>N:
                break
            if player_stage>j:
                game[j].challenge+=1
                game[j].success+=1
            elif player_stage==j:
                game[j].challenge+=1
    for i in range(1, N + 1):
        if game[i].challenge == 0:
            game[i].ratio = 0
        else:
            game[i].ratio = (game[i].challenge - game[i].success) / game[i].challenge
    sorted_game = sorted(game.items(), key=lambda x: (-x[1].ratio, x[1].diff))
    answer = [item[0] for item in sorted_game]
    return answer