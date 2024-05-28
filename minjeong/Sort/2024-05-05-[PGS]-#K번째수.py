def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start = commands[i][0]-1
        end = commands[i][1]
        k = commands[i][2]-1
        temp = array[start:end]
        temp.sort()
        answer.append(temp[k])
    return answer
'''
# 다른 코드
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
'''