# 내 풀이 
N = int(input())

# 5kg 봉지의 최대 개수 
five = N //5

while five >= 0:
    # 남은 무게
    remain = N - (five * 5)
    
    # 남은 무게가 3의 배수라면
    if remain % 3 == 0:
        # 3kg 봉지의 최대 개수
        three = remain // 3
        print(five + three) # 총 봉지 수 출력
        break
    five -= 1 # 5kg 봉지의 개수를 줄여가며 확인

else:
    print(-1) # 모든 경우를 시도해도 나누어 떨어지지 않으면 -1 출력

# 다른 풀이 1
n = int(input())

if n % 5 == 0:  
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2: 
            print(-1)
            break
        elif n == 0:  
            print(p)
            break

# 다른 풀이 2
num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += int(num // 5)
    print(count)
    break
  
  num -= 3
  count += 1
  
else:
  print(-1)
