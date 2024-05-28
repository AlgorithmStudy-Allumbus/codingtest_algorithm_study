def solution(n, lost, reserve):
    answer = 0
    # 집합을 이용해서 중복값 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    # 빌려줄 수 있는지 판단
    for can in list(reserve_set):
        if can-1 in lost_set:
            lost_set.remove(can-1)
        elif can+1 in lost_set:
            lost_set.remove(can+1)

    # 정답은 전체 학생 수에서 잃어버린 학생 수를 빼는 것
    answer = n - len(list(lost_set))
    return answer