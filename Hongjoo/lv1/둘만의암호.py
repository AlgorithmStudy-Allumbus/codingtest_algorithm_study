def solution(s, skip, index):
    li =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    sub_li = list(skip)
    # 1.res_li = li - list(skip) // Difference 
    res_li = [x for x in li if x not in sub_li]
    input = list(s)
    answer = ''
    #2. find matching element's index(k) and add "index"
    # if the adding index is out of range ,using mod
    for i in range(len(input)):
        for k in range(len(res_li)):
            if input[i] == res_li[k]:
                answer += res_li[(k+index)%len(res_li)]
                break
    return answer