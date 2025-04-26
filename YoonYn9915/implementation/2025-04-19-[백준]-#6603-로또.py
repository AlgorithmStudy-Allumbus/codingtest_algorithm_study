import sys
from itertools import combinations

inp = sys.stdin.readline

while True:
    arr = list(map(int, inp().split()))

    # 0이면 종료
    if arr[0] == 0:
        break
    # 0이 아니면
    K = arr[0]
    # combinations 라이브러리를 사용해 집합 S에서 조합 생성
    answers = combinations(arr[1:K+1], 6)

    for answer in answers:
        for num in answer:
            print(num, end=' ')
        print()

    print()