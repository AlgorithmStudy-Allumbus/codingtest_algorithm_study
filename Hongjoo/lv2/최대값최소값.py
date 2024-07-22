def solution(s):
    answer = ''
    li = list(map(int,s.split(" ")))
    li.sort() # 오름 차순 정렬
    answer= str(li[0]) + " "+str(li[-1]) #"최소 최대"
    # print(answer)
    return answer