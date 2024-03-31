def solution(A, B):
    answer = 0
    A.sort(); B.sort()
    lenA, lenB = len(A), len(B)
    Ap, Bp = 0, 0
    
    while Bp < lenB and Ap < lenA:
        if A[Ap] < B[Bp]:
            answer += 1
            Ap += 1
            Bp += 1
        elif A[Ap] == B[Bp]:
            #Ap += 1
            Bp += 1
        elif A[Ap] > B[Bp]:
            Bp += 1
    print(answer)
    return answer