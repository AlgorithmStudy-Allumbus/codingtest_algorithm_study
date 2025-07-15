"""
풀이1
"""
def solution(n):
    """
    이동방법
    1. K칸 앞으로 점프 => 건전지 사용량 -K
    2. 순간이동: (현재까지 온 거리) * 2 => 건전지 사용량 X
    목표
    - 거리가 N만큼 떨어져있는 장소로 간다고 했을 때 건전지 사용량의 최솟값을 구하기
    """
    ans = 0
    while n > 0:
        if (n % 2 == 0):
              n //= 2
        else:
            n -= 1
            ans += 1
    return ans

"""
풀이2
"""
def solution(n):
    return bin(n).count('1')