def solution(s):
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    answer = 1
    def expand(left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1
    for i in range( len(s)-1):
        len_odd=expand(i, i)
        len_even=expand(i,i+1)
        answer=max(len_odd, len_even, answer)
    return answer