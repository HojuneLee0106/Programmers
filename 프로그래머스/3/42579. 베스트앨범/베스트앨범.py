def solution(genres, plays):
    answer = []
    dict={}
    c={}
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]]=[(plays[i],i)]
            c[genres[i]]=plays[i]
        else:
            c[genres[i]]+=plays[i]
            dict[genres[i]].append((plays[i],i))
            dict[genres[i]].sort(key=lambda x:(-x[0],x[1]))
            if len(dict[genres[i]]) > 2:
                dict[genres[i]].pop()
    print(dict)         
    while dict:
        song=max(c, key=c.get)
        for p,i in dict[song]:
            answer.append(i)
        del dict[song]
        del c[song]
    return answer