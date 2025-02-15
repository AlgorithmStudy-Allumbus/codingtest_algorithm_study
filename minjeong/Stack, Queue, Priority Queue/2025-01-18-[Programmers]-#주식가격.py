def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx, p in enumerate(prices):
        while stack and (p < prices[stack[-1]] or idx == len(prices) - 1):
            last = stack.pop()
            answer[last] = idx - last
        stack.append(idx)

    return answer