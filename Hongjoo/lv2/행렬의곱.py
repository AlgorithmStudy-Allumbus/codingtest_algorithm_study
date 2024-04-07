def solution(arr1, arr2):
    answer = [[]]
    s_li = []
    s1=0
    for r1 in range(len(arr1)):
        for c2 in range(len(arr2[0])):
            for c1 in range(len(arr1[r1])):
                r2 = c1
                x = arr1[r1][c1]*arr2[r2][c2]
                s1+=x
            s_li.append(s1)
            s1 = 0
        answer.append(s_li)
        s_li=[]
    del answer[0]

    return answer