import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        // 1) 작업 큐: 인덱스(idx)와 우선순위(priority)를 함께 보관
        Queue<DTO> queue = new LinkedList<>();

        // 2) 우선순위 큐: 남아있는 작업 중 가장 높은 우선순위를 꺼내기 위함
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0 ; i < priorities.length; i++) {
            queue.offer(new DTO(i, priorities[i]));
            pq.offer(priorities[i]);
        }

        // System.out.println(queue);
        // System.out.println(pq);

        int count = 0; // 실행된 작업 수

        while(!queue.isEmpty()) {
            DTO cur = queue.poll(); // 현재 작업 꺼냄

            // 현재 작업 우선순위가 남은 작업의 최고 우선순위와 같다면
            if(cur.priority == pq.peek()) {
                count++;
                pq.poll(); // 우선순위 큐에서 제거
                // 내가 찾던 작업이라면 실행 순서 반환
                if (cur.idx == location) {
                    return count;
                }
            }
            else {
		            // 우선순위가 더 높은 작업이 남아있다면 뒤로 재삽입
                queue.offer(cur);
            }
        }
        return count;
    }

    // 인덱스 + 우선순위를 함께 보관할 DTO
    static class DTO {
        int idx;
        int priority;
        DTO(int idx, int priority) {
            this.idx = idx;
            this.priority = priority;
            // System.out.println("idx: "+idx+" priority: "+priority);
        }
    }
}