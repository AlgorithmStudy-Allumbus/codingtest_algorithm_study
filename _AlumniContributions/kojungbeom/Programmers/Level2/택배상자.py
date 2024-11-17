def solution(record):
    answer = []
    id2nick = {}
    command = []
    for r in record:
        #print(r.split(' '))
        rlist = r.split(' ')
        
        if rlist[0] == "Change" or rlist[0] == "Enter":
            id2nick[rlist[1]] = rlist[2]
        
        command.append([rlist[0], rlist[1]])
        
    
    
    for c in command:
        com, id = c
        if com == "Enter":
            sentence = f'{id2nick[id]}님이 들어왔습니다.'
            answer.append(sentence)
        elif com == "Leave":
            sentence = f'{id2nick[id]}님이 나갔습니다.'
            answer.append(sentence)
    
    return answer