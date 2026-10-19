def solution(dirs):
    x=0
    y=0
    dict={}
    answer = 0
    for i in range(len(dirs)):
        if dirs[i]=="U":
            if y+1>5:
                continue
            else:
                if (x,y) not in dict:
                    if (x,y+1) in dict and (x,y) in dict[(x,y+1)]:
                        y+=1
                        continue
                    dict[(x,y)]=[(x,y+1)]
                    y+=1
                    answer+=1
                else:
                    if (x,y+1) in dict[(x,y)]:
                        y+=1
                    elif (x,y+1) in dict and (x,y) in dict[(x,y+1)]:
                        y+=1
                        continue
                    else:
                        dict[(x,y)].append((x,y+1))
                        y+=1
                        answer+=1
        elif dirs[i]=="D":
            if y-1<-5:
                continue
            else:
                if (x,y) not in dict:
                    if (x,y-1) in dict and (x,y) in dict[(x,y-1)]:
                        y-=1
                        continue
                    dict[(x,y)]=[(x,y-1)]
                    y-=1
                    answer+=1
                else:
                    if (x,y-1) in dict[(x,y)]:
                        y-=1
                    elif (x,y-1) in dict and (x,y) in dict[(x,y-1)]:
                        y-=1
                        continue
                    else:
                        dict[(x,y)].append((x,y-1))
                        y-=1
                        answer+=1
        elif dirs[i]=="L":
            if x-1<-5:
                continue
            else:
                if (x,y) not in dict:
                    if (x-1,y) in dict and (x,y) in dict[(x-1,y)]:
                        x-=1
                        continue
                    dict[(x,y)]=[(x-1,y)]
                    x-=1
                    answer+=1
                else:
                    if (x-1,y) in dict[(x,y)]:
                        x-=1
                    elif (x-1,y) in dict and (x,y) in dict[(x-1,y)]:
                        x-=1
                        continue
                    else:
                        dict[(x,y)].append((x-1,y))
                        x-=1
                        answer+=1
        else:
            if x+1>5:
                continue
            else:
                if (x,y) not in dict:
                    if (x+1,y) in dict and (x,y) in dict[(x+1,y)]:
                        x+=1
                        continue
                    dict[(x,y)]=[(x+1,y)]
                    x+=1
                    answer+=1
                else:
                    if (x+1,y) in dict[(x,y)]:
                        x+=1
                    elif (x+1,y) in dict and (x,y) in dict[(x+1,y)]:
                        x+=1
                        continue
                    else:
                        dict[(x,y)].append((x+1,y))
                        x+=1
                        answer+=1
    return answer