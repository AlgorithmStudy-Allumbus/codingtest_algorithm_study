def solution(sequence, k):
    left, right = 0, 0
    lenS = len(sequence)
    answer = [0, lenS]
    sum_permute = sequence[0]

    while True:
        if sum_permute < k:
            right += 1
            if right == lenS:
                break
            sum_permute += sequence[right]
        else:
            if sum_permute == k:
                if right - left < answer[1]-answer[0]:
                    answer = [left, right]
            sum_permute -= sequence[left]
            left += 1
    return answer