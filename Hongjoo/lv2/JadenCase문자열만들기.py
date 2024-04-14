def solution(s):
    #1. words(" ") 
    # first letter : Big 
    # others : small
    #연속 띄어쓰기 :가능
    answer = []
    small = s.lower()
    s_li = list(small)
    for i in range(len(s_li)):
        #upper
        #1.first letter
        if i == 0 : 
            s_li[i]=s_li[i].upper()
        #2. word's first letter 
        if s_li[i] == " ":
            if s_li[i+1].islower():
                s_li[i+1] = s_li[i+1].upper()
        #number issue : " " +number + str 
        if s_li[i].isnumeric() and i!=0 :
            if s_li[i+1].isnumeric():
                continue
            if s_li[i+1]== " "and s_li[i+2].isalpha():
                del s_li[i+1]
            if s_li[i-1] != " " :
                s_li.insert(i," ")
    answer="".join(s_li)
    print(answer)
    return answer