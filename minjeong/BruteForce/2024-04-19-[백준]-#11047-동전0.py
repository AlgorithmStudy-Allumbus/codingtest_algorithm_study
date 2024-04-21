n, k = map(int, input().split()) # n: 동전의 종류 k: 가치의 합
coin_type = [] # 동전의 종류를 나타내는 리스트
count = 0 # 동전 개수를 저장할 변수

for _ in range(n): # 동전 종류 입력하여 리스트에 저장
    coin = int(input())
    coin_type.append(coin)

coin_type.sort(reverse=True) # 동전 종류를 동전의 값이 큰 순서대로 (역순으로) 정렬

for i in range(n):
    if (k // coin_type[i] ): # 몫이 존재한다면 아래 조건문 실행
        mok = k // coin_type[i] # 몫을 구하여 저장
        count += mok # 몫만큼 동전 개수에 더하기
        k -= coin_type[i] * mok # 원래 값인 k에는 그만큼 빼주기
print(count) # 정답 출력