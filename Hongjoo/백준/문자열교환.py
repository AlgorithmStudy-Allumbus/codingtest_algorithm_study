"""
https://www.acmicpc.net/problem/1522
"""

words= input()
window_size = words.count("a") # 1. a의 개수 = sliding window 크기
result = 999999999 

# 원형 문자열
words += words[0:window_size-1]
# 2. 최대한 a 가 연속해 있는 idx 범위 찾기
for start in range(len(words) - (window_size-1)):
    result = min(result, words[start: start+ window_size].count("b"))

print(result)