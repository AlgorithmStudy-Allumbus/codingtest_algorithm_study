def solution(files):
    answer = []
    temp = []
    for idx, f in enumerate(files):
        number_start = 0
        number_end = len(f)
        flag1 = True
        flag2 = True
        for i, c in enumerate(f):
            cisdigit = c.isdigit()
            if cisdigit:
                if flag1:
                    number_start = i
                    flag1 = False
            elif not cisdigit and not flag1:
                if flag2:
                    flag2 = False
                    number_end = i
        #print(f, number_start, number_end)
        temp.append([idx, f[:number_start].lower(), int(f[number_start:number_end])]) 
                    
        
    
    temp.sort(key=lambda x:(x[1], x[2]))
    for t in temp:
        answer.append(files[t[0]])

    return answer