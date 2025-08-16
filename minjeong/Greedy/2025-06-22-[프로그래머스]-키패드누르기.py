def solution(numbers, hand):
    answer = ''
    pad = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
           '4': (1, 0), '5': (1, 1), '6': (1, 2),
           '7': (2, 0), '8': (2, 1), '9': (2, 2),
           '*': (3, 0), '0': (3, 1), '#': (3, 2)
           }

    left = pad['*']
    right = pad['#']

    for num in numbers:
        # 왼손이 눌러야 하는 번호
        if num in (1, 4, 7):
            answer += 'L'
            left = pad[str(num)]
        # 오른손이 눌러야 하는 번호
        elif num in (3, 6, 9):
            answer += 'R'
            right = pad[str(num)]
        # 가운데 번호일 경우 (2, 5, 8, 0)
        else:

            # 해당 번호와 왼손 거리
            left_dist = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            # 해당 번호와 오른손 거리
            right_dist = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])

            # 더 가까운 거리
            if left_dist < right_dist:
                answer += 'L'
                left = pad[str(num)]
            elif left_dist > right_dist:
                answer += 'R'
                right = pad[str(num)]
            # 왼손과 오른손 거리가 같을 경우
            else:
                if hand == 'right':
                    answer += 'R'
                    right = pad[str(num)]
                else:
                    answer += 'L'
                    left = pad[str(num)]

    return answer