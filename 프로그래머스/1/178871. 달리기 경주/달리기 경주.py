def solution(players, callings):
    dict={player: i for i, player in enumerate(players)}
    for i in callings:
        current=dict[i]
        front=current-1
        front_p=players[front]
        dict[front_p]=current
        dict[i]=front
        players[current]=front_p
        players[front]=i
    return players