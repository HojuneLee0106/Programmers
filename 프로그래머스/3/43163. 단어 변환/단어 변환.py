from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = []
    queue=deque()
    queue.append((begin,words,0))
    while queue:
        word, l, c=queue.popleft()
        if word==target:
            answer.append(c)
        for i in range(len(l)):
            change=0
            pos=True
            for j in range(len(words[i])):
                if change>=2:
                    pos=False
                    break
                if word[j]!=l[i][j]:
                    change+=1
            if pos and change==1:
                new_l=l[:]
                new_word=new_l.pop(i)
                k=c+1
                queue.append((new_word,new_l,k))
    print(answer)
    if len(answer)==0:
        return 0
    else:
        return min(answer)