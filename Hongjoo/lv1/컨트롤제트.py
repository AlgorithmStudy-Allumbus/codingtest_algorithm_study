def solution(s):
    answer = 0
    tmp = []
    # 1. delete blank and change type spring to list
    s=s.split() 
    for i in range(len(s)):
        # if z exist, then pop all elements in tmp
        if s[i] == "Z":
            tmp.pop()
            continue
        tmp.append(s[i])
    # sum about tmp
    sum = 0
    for i in range(len(tmp)):
        sum+= int(tmp[i])
        print(sum)
    answer = sum
    return answer
