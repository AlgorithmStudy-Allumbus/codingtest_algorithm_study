import sys
input = sys.stdin.readline

# 이길 수 있는지 확인하는 함수
def can_win(a, b): # 기준, 비교대상
    if (a == "S" and b == "P") or (a == "R" and b == "S") or (a == "P" and b == "R"):
        return True
    return False # 상대방과 비기거나 상대방이 이길 경우는 False

ML, MR, TL, TR = map(str, input().split())

# 민성이가 무조건 이길 수 있는지 확인
ms_can_win = (can_win(ML, TL) and can_win(ML, TR)) or (can_win(MR, TL) and can_win(MR, TR))

# 태경이가 무조건 이길 수 있는지 확인
tk_can_win = (can_win(TL, ML) and can_win(TL, MR)) or (can_win(TR, ML) and can_win(TR, MR))

# 정답 출력
if ms_can_win:
    print("MS")
elif tk_can_win:
    print("TK")
else:
    print("?")