def solution(user_id, banned_id):
    # [j_idx, current]
    answer = set()
    lenU, lenB = len(user_id), len(banned_id)
    stack = [[0, [], [0] * lenU, [0] * lenB]]
    
    while stack:
        j_idx, current, uvisited, bvisited = stack.pop()
        if len(set(current)) == len(banned_id):
            answer.add(tuple(sorted(current)))
            continue
        
        for i in range(lenU):
            for j in range(j_idx, lenB):
                if not uvisited[i] and not bvisited[j]:
                    condition1 = len(user_id[i]) == len(banned_id[j])
                    condition2 = True
                    for a, b in zip(user_id[i], banned_id[j]):
                        if b != '*' and a != b:
                            condition2 = False
                            break
                    if condition1 and condition2:
                        new_uvisited = uvisited[:]
                        new_bvisited = bvisited[:]
                        new_bvisited[j] = new_uvisited[i] = True
                        new_stack = current[:]
                        new_stack.append(user_id[i])
                        stack.append([j+1, new_stack, new_uvisited, new_bvisited])
    #print(answer)
    return len(answer)


def is_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for u, b in zip(user_id, banned_id):
        if b != '*' and u != b:
            return False
    return True

def count_unique_combinations(user_id, banned_id, idx, used, used_banned, result, results):
    if idx == len(banned_id):
        results.add(tuple(sorted(result)))
        return
    
    for i, user in enumerate(user_id):
        if not used[i] and is_match(user, banned_id[idx]):
            used[i] = True
            result.append(user)
            count_unique_combinations(user_id, banned_id, idx + 1, used, used_banned, result, results)
            result.pop()
            used[i] = False

def solution(user_id, banned_id):
    results = set()
    count_unique_combinations(user_id, banned_id, 0, [False] * len(user_id), [False] * len(banned_id), [], results)
    return len(results)