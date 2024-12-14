#2024.12.14, 30min
def solution(record):
    answer = []
    # 1. history와 user_db  DB 정의 
    user_db = {} # key=uid , value = username
    history = [] # ["Enter / Leave" , uid ]
    
    #2. history와 user_db 기록 시작 
    for r in record :
        command = r.split() # command = [동사V ,userid ,(username)]
        v = command[0] 
        uid = command[1]
         # 2-1 Enter : user_db 추가 , history 추가
        if v == 'Enter' :
            user_db[uid] = command[2] # user_db[uid] = username
            history.append([uid ,v]) # history: [uid , "Enter" ]
        #2-2 Leave :history 추가
        elif v == 'Leave':
            history.append([uid,v]) # history: [uid , "Leave" ]
        #2-3 Change : user_db 수정(username 변경)
        elif v == 'Change': 
            user_db[uid] = command[2] #user_db[uid] = new_username
    
    # 3.user_db, histoy 기반으로 문자열 배열 result를 만들기         
    result = list()
    # 영어 v 을 한국어 동사로 번역
    en_to_ko = {'Enter':'들어왔습니다.','Leave' : '나갔습니다.'} 
    for uid , h_v in history : 
        user_name = user_db[uid]
        result.append(f"{user_name}님이 {en_to_ko[h_v]}" )
    
    return result