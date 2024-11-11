"""
#Q1: 좌표평면의 경계를 넘어서는 커멘드도 존재하나요?
    -> 이 경우 예외처리가 필요하기 떄문..!
My solution:
    일단 이 문제는 커멘드대로 좌표평면상에서 움직이도록
    만들면되는 간단한 문제로 보이는데..
    이때 "처음 걸어본 길의 길이"를 구하는 것이기 때문에
    처음 간건지 아닌지를 판별할 무언가가 필요하다.
    이를 위한 조건문과 메모리 역할을 할 변수를 만들어서
    걸어본 길의 길이를 카운팅하는 방식으로 풀 수 있을것 같다.
    그래서 나는 먼저 좌표평면을 나타낼수있는 2차원 배열을 만들것이다.
    이 배열의 성분은 0과 1로 표시되는데, 0은 걸어본 길이 아닐 경우이고
    1은 걸어본길일 경우에 해당한다. -> 이 부분은 잘못 생각함..
    결국 커멘드에 따라 2차원배열의 row와 col의 성분을 검사하면서 카운팅하는
    방식으로 코드를 짜보려고한다.
"""
def solution(dirs):
    answer = 0
    ddict = {"U": (1, 0), "D":(-1,0), "R":(0,1), "L":(0,-1)}
    seen = set()
    row, col = 0+5, 0+5
    
    for d in dirs:
        r, c = ddict[d]
        new_row = row + r
        new_col = col + c
        if 0<=new_row<=10 and 0<=new_col<=10:
            seen.add((row, col, new_row, new_col))
            seen.add((new_row, new_col, row, col))
            row = new_row
            col = new_col
    return len(seen) // 2