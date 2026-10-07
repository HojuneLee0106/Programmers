def solution(ingredient):
    answer = 0
    ham=[]
    for i in ingredient:
        ham.append(i)
        if len(ham)>=4:
            if ham[-4:]==[1,2,3,1]:
                answer+=1
                for j in range(4):
                    ham.pop()
        
    return answer