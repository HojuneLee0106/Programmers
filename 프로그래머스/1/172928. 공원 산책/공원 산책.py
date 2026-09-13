def solution(park, routes):
    height = len(park)
    width = len(park[0])
    x=0
    y=0
    for i in range(len(park)):
        if "S" in park[i]:
            for j in range(len(park[i])):
                if park[i][j]=="S":
                    y=i
                    x=j
    def move(d,l,x,y):
        if d=="E":
            if x+l>=width:
                return x,y
            else:
                for i in range(1,l+1):
                    if park[y][x+i]=="X":
                        return x,y
                x+=l
                return x,y
        elif d=="W":
            if x-l<0:
                return x,y
            else:
                for i in range(1,l+1):
                    if park[y][x-i]=="X":
                        return x,y
                x-=l
                return x,y
        elif d=="S":
            if y+l>=height:
                return x,y
            else:
                for i in range(1,l+1):
                    if park[y+i][x]=="X":
                        return x,y
                y+=l
                return x,y
        else:
            if y-l<0:
                return x,y
            else:
                for i in range(1,l+1):
                    if park[y-i][x]=="X":
                        return x,y
                y-=l
                return x,y
    for i in range(len(routes)):
        d,l=routes[i].split(" ")
        l=int(l)
        x,y=move(d,l,x,y)
    answer = [y,x]
    return answer