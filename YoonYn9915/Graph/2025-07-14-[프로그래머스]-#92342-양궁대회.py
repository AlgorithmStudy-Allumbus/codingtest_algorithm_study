'''
요구사항
- k (1~10)점을 어피치가 a발을 맞췄고, 라이언이 b발을 맞혔을 때, b> a이면 k점을 라이언이 가져가고, 아니면 어피치가 k점을 가져간다. 단 a = b = 0일 경우 누구도 k점을 가져가지 못한다.
- 모든 과녁에 대하여 두 선수의 총점 계산, 단 최종 점수가 같으면 어피치를 우승자로
- 어피치가 n발을 쏜 후 그 정보를 가지고 라이언이 어피치를 가장 큰 점수차로 이기기 위해 n발을 어떻게 맞춰야 하는지 구해라.
- 라이언이 우승할 수 없는 경우 -1을 출력하고, 라이언이 가장 큰 점수차로 이길 수 있는 방법이 여러개인 경우 가장 낮은 점수를 더 많이 맞힌 경우를 반환해야 한다.


아이디어
- 이 문제는 greedy는 아닌거 같다. greedy로 하려면 큰 점수를 무조건 먹기 위해 어피치가 쏜 화살 + 1만큼 할 텐데 입출력 예 1번처럼 라이언이 10점을 먹어도 9점 8점을 어피치가 먹으면 라이언이 지게 된다.
- 따라서 완전 탐색을 진행해야 하며, dfs와 backtracking을 사용하여 깊이 우선으로 모든 경우의 수 계산.
- 양궁대회 시뮬레이션 아이디어: info(어피치의 결과 배열)가 10점부터 0점까지의 나열이므로 10점부터 0점까지 내림차순으로 화살을 쏜다. 모든 경우를 구할 수 없으므로 현재 점수에 대해 라이언이 0발 혹은 info[i] + 1발을 맞춘 경우만 고려하고 나머지 경우는 진행하지 않는다. 즉 어피치가 10점에 2발을 맞췄다면, 라이언은 0발을 맞추고 화살을 아껴 다음 점수로 가던지, 2+1발을 맞춰 화살을 쓰더라도 점수를 얻고 가던지 두가지 경우만 해야 한다.


구현
1. dfs 진행
    - dfs 종료 조건: 현재 점수판이 0점이거나, 남은 화살이 없을때
    - dfs 진행: (점수 그대로, 화살개수 그대로) 혹은 (현재 점수 먹기, 화살개수 소모하기)                   두가지 버전으로 나뉨
2. 라이언과 어피치 중 누가 얼마의 차이로 이겼는지 확인하는 함수
    - 차이가 같다면 가장 낮은 점수를 더 많이 맞춘 배열 선택

'''

# 점수차가 같은 경우 가장 낮은 점수를 많이 쏜 것을 정답으로
def choose_answer(arr1, arr2):
    length = len(arr1)

    # 낮은 점수부터 체크해야 하니까 역순으로
    for i in range(length-1, -1, -1):
        if arr1[i] > arr2[i]:
            return arr1
        elif arr2[i] > arr1[i]:
            return arr2

    # 반복문이 끝났는데 여기까지 온 경우는 두 배열이 같다는 뜻이므로 아무거나 반환
    return arr1



# 승자와 점수차를 반환.
def get_winner(lion, appeach):
    lion_score = 0
    appeach_score = 0
    length = len(appeach)
    for i in range(length):
        if lion[i] > 0 or appeach[i] > 0:
            # 라이언이 맞춘 화살이 어피치보다 많으면 라이언이 점수를 가져오고
            if lion[i] > appeach[i]:
                lion_score += (10 -i)
            # 그렇지 않으면 어피치가 점수를 가져온다.
            else:
                appeach_score += (10 - i)

    # 라이언 승
    if lion_score > appeach_score:
        return 1, lion_score - appeach_score
    else:
        return -1, appeach_score - lion_score

def dfs(n, idx, lion, appeach):
    global max_result, answer

    # dfs 종료 조건. 현재 점수판이 0점이거나, 남은 화살이 없을 때
    if n == 0 or idx == 10:
        # 점수판이 0점이면 라이언의 남은 화살 모두 0점에 맞춤
        if idx == 10:
            lion[idx] = n

        # 둘 중 누가 승자인지 판단하고, 라이언이 승자면 최대점수인지 확인
        winner, score_gap = get_winner(lion, appeach)

        # 라이언이 승자이면
        if winner == 1:
            if max_result < score_gap:
                max_result = score_gap
                answer = lion
            elif max_result == score_gap:
                answer = choose_answer(answer, lion)
        return

    # 현재 점수를 포기하고 화살을 아껴서 다음 dfs 진행
    dfs(n, idx+1, lion[:], appeach)

    # 어피치보다 한 발 더 쏴서 현재 점수를 먹고 다음 dsf 진행
    if n >= appeach[idx] + 1:
        tmp = lion[:]
        tmp[idx] = appeach[idx] + 1
        dfs(n - (appeach[idx] + 1), idx+1, tmp, appeach)




def solution(n, info):
    global answer, max_result
    # 라이언이 맞춘 점수 초기화
    lion = [0] * 11
    # 정답이 될 배열
    answer = [0] * 11

    max_result = 0

    # 10점부터 0점까지 점수판을 내림차순으로 순회하며 몇 발을 맞췄는지 시뮬레이션 하기 위함.
    # n은 남은 화살, idx는 현재 점수판(0이면 10점, 10이면 0점)
    dfs(n, 0, lion, info)

    if max_result == 0:
        print([-1])
    else:
        print(answer)


solution(10,	[0,0,0,0,0,0,0,0,3,4,3])
