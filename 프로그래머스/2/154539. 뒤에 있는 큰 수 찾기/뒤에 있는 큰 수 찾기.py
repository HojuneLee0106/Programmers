def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        if i==len(numbers)-1:
            answer.append(-1)
            break
        c=1
        N=len(answer)
        for j in range(i+1,len(numbers)):
            if numbers[j]<=numbers[i]:
                c+=1
            else:
                stack=[numbers[j] for _ in range(c)]
                answer+=stack
                i+=c-1
                break
        M=len(answer)
        if N==M:
            answer.append(-1)
    return answer