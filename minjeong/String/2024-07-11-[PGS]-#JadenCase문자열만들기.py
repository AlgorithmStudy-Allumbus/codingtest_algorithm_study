def solution(s):
    answer = ''
    s = s.lower()
    
    if s[0].isdigit():
        answer += s[0]
    else:
        answer += s[0].upper()
    
    for i in range(1, len(s)):
        if s[i-1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i]

    return answer