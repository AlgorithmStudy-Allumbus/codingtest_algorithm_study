"""
[백준#1522.문자열 교환.py]
https://www.acmicpc.net/problem/1522

# 문자열 , 투 포인터

"""
# 1. a의 개수 = sliding window 크기
words= input()
window_size = words.count("a")
result = 999999999 

# 원형 문자열
words += words[0:window_size-1]
# 슬라이싱 된 문자열 속 b의 개수 최소값
for start in range(len(words) - (window_size-1)):
    result = min(result, words[start: start+ window_size].count("b"))

print(result)