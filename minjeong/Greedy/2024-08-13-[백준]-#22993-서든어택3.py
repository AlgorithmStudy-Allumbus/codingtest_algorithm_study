import sys
input = sys.stdin.readline

n = int(input())
power = list(map(int, input().split()))

# 준원이를 제외한 나머지 플레이어들의 공격력을 정렬한다.
others = sorted(power[1:])

# 준원이의 초기 공격력
junwon = power[0]

# 나머지 플레이어들과 비교하면서 주원이의 최종 생존 가능 여부를 판단
for p in others:
    if junwon > p:
        junwon += p
    else:
        print("No")
        exit()

# 모든 플레이어를 이겼다면 "Yes"를 출력
print("Yes")