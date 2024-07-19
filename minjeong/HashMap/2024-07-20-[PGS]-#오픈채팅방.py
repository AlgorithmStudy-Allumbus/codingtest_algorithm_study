def solution(record):
    answer = []
    dict = {}
    
    # 사용자 DB 딕셔너리
    for i in range(len(record)):
        temp = record[i].split()
        if temp[0] == 'Enter' or temp[0] == 'Change':
            dict[temp[1]] = temp[2]
    
    # Enter, Change, Leave 순회
    for i in range(len(record)):
        temp = record[i].split()
        if temp[0] == 'Enter':
            answer.append(f"{dict[temp[1]]}님이 들어왔습니다.")
        elif temp[0] == 'Leave':
            answer.append(f"{dict[temp[1]]}님이 나갔습니다.")

        
    return answer