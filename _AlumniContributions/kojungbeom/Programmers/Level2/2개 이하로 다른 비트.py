def solution(numbers):
    answer = []
    for n in numbers:
        n_str = list(str(bin(n)).replace('0b', ''))
        flag = False
        for i in range(len(n_str)-1, -1, -1):
            if n_str[i] == '0':
                if i == len(n_str)-1:
                    flag = True
                    n_str[i] = '1'
                    break
                elif n_str[i] == '0' and n_str[i+1] == '1':
                    n_str[i], n_str[i+1] = n_str[i+1], n_str[i]
                    flag = True
                    break
        n_str = ''.join(n_str)
        if not flag:
            n_str = '10' + n_str[1:]
        answer.append(int(n_str, 2))

    return answer