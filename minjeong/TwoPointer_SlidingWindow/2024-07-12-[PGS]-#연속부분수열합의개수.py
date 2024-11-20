def solution(elements):
    n = len(elements)
    elements.extend(elements)  # 원형 수열을 위해 배열을 두 배로 확장

    sums = set()  # 중복을 피하기 위해 set 사용

    for length in range(1, n + 1):  # 부분 수열의 길이
        for start in range(n):  # 시작 인덱스
            sub_sum = sum(elements[start:start + length])  # 부분 수열의 합 계산
            sums.add(sub_sum)  # set에 추가

    return len(sums)  # 서로 다른 부분 수열 합의 개수 반환