def solution(topping):
    answer = 0
    cdict = {}
    bdict = {}

    for t in topping:
        if t in bdict:
            bdict[t] += 1
        else:
            bdict[t] = 1

    for t in topping:
        bdict[t] -= 1
        if bdict[t] == 0:
            del bdict[t]

        if t in cdict:
            cdict[t] += 1
        else:
            cdict[t] = 1

        if len(bdict) == len(cdict):
            answer += 1
        elif len(bdict) < len(cdict):
            break
    return answer