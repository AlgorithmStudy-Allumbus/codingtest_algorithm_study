"""
- 작은 수가 위로 올라감
조건 
1. 한번에 한개만 옮기기 가능
2, 큰원판 은 아래 , 작은 원판은 위
3. 기둥 3개 
# 재귀
goal : 기둥 1 -> 기둥 3으로 옮기는 방법 최소 방법
#flow
1.  (n-1)개 원판 start   => 중앙 (재귀) 몰아 넣기
2. n 번째 원판 : start -> target  이동
3. (n-1) 개 원판 중앙 -> target (재귀) 몰아 넣기


"""
answer = []
def hannoi(src ,target , inter , n) : 
    if n== 1 : 
        answer.append([src, target])
    else :
        hannoi(src , inter , target , n-1)
        hannoi(src, target , inter , 1)
        hannoi(inter, target, src , n-1)

def solution(n):
    
    hannoi(1 ,3 , 2 , n)
    
    return answer