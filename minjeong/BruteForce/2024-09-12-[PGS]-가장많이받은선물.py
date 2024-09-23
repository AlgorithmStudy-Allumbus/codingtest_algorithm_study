# PGS. 2024 KAKAO WINTER INTERNSHIP - 가장 많이 받은 선물
def solution(friends, gifts):
    gift_map = {}  # 각 친구 쌍 간 선물 기록
    send_count = {}  # 선물 준 횟수 딕셔너리
    receive_count = {}  # 선물 받은 횟수 딕셔너리
    gift_count = {}  # 선물 지수 딕셔너리
    next_month_gift_cnt = {}  # 다음 달에 받을 선물의 개수를 친구들별로 저장하는 딕셔너리

    for friend in friends: # 초기화
        gift_map[friend] = {}
        send_count[friend] = 0
        receive_count[friend] = 0
        gift_count[friend] = 0
        next_month_gift_cnt[friend] = 0

    # 선물 기록 분석(각 친구 간에 누가 몇 번 선물을 주고받았는지)
    for gift in gifts:
        sender, receiver = gift.split()
        if receiver not in gift_map[sender]: # 해당 친구 간의 기록이 없다면 0으로 초기화
            gift_map[sender][receiver] = 0
        if sender not in gift_map[receiver]: # 해당 친구 간의 기록이 없다면 0으로 초기화
            gift_map[receiver][sender] = 0
        gift_map[sender][receiver] += 1 # sender가 receiver에게 선물한 횟수 +1

        send_count[sender] += 1         # sender가 준 선물 횟수 +1
        receive_count[receiver] += 1    # receiver가 받은 선물 횟수 +1

    # 선물 지수 계산
    for friend in friends:
        # 선물지수: 준 선물 수 - 받은 선물 수
        gift_count[friend] = send_count[friend] - receive_count[friend]

    # 모든 친구 쌍을 비교하여 다음 달에 받을 선물 수 계산
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            A = friends[i]
            B = friends[j]
            if gift_map[A].get(B, 0) > gift_map[B].get(A, 0): # A>B이면, A가 다음달에 받음
                next_month_gift_cnt[A] += 1
            elif gift_map[A].get(B, 0) < gift_map[B].get(A, 0): #A<B이면, B가 다음달에 받음
                next_month_gift_cnt[B] += 1
            else:  # 두 사람이 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 받음
                if gift_count[A] > gift_count[B]:
                    next_month_gift_cnt[A] += 1
                elif gift_count[A] < gift_count[B]:
                    next_month_gift_cnt[B] += 1
                # 선물 지수도 같다면 아무도 받지 않음

    # 가장 많이 받을 친구 반환
    return max(next_month_gift_cnt.values())