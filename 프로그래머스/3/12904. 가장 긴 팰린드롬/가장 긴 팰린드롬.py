def solution(s):
    answer = 1
    for i in range(len(s)-1):
        end=len(s)-1
        while i<=end:
            if s[i]==s[end]:
                pos=True
                for j in range(i,i+(end-i)//2+1):
                    if s[j]!=s[end-(j-i)]:
                        pos=False
                        break
                if pos:
                    answer=max(answer, end-i+1)
                    break
                else:
                    end-=1
            else:
                end-=1
    return answer