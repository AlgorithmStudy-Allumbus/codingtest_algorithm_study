def solution(k, dungeons):
    max_count = 0 
    def brutefoce(path, life):
        nonlocal max_count 
        for idx in range(len(dungeons)):
            # (유망 여부) 조건에 안 맞으면 건너뛰기 : limit 제한 , 중복 탐사 방지
            if dungeons[idx][0] <= life and  idx not in path:
                # 3. 탐색할 노드 선택 - 상태 변화  
                path.append(idx)
                # 4. 재귀 호출(담 단계) - 자식 노드로 이동
                brutefoce(path ,life -dungeons[idx][1])
                # 5. 선택 취소 - 부모 노드로 복귀
                path.pop()
        max_count = max(max_count , len(path))
    brutefoce([], k )

    return max_count