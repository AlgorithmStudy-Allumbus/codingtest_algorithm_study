str = input() 

# 'a'의 개수 
a_count = str.count('a')

# 'b'의 개수 
current_b = 0 
for i in range(a_count):
    if str[i] == 'b':
        current_b += 1 

min_b = current_b 

# 고정된 길이의 구간별 탐색  
for i in range(1, len(str)):
    # 이전 문자를 제거 
    if str[i-1] == 'b': 
        current_b -= 1 
    # 새 문자를 추가 
    if str[(i + a_count - 1) % len(str)] == 'b':
        current_b +=1
    min_b = min(min_b, current_b)

print(min_b)
