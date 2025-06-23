"""
https://programmers.co.kr/learn/courses/30/lessons/12911
"""
def solution(n):
    answer= 0
    bin_flag= True
    one = list(str(bin(n))).count("1")
    while bin_flag :
        n+=1
        bin_flag = not(str(bin(n))[2:].count("1") == one)
    answer=n 
        
    
    return answer