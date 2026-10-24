def solution(elements):
    answer = set()
    length=len(elements)
    elements+=elements
    for j in range(length):    
        for i in range(1,length+1):
            window=sum(elements[j:j+i])
            if window not in answer:
                answer.add(window)
        
            
    return len(answer)