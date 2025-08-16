import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {

        Queue<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);    // 처음에 빈 칸으로 채워둔다.
        }

        int time = 0;    // 전체 경과 시간
        int current = 0;       // 다리 위 현재 무게 합
        int idx = 0;        // 다음에 보낼 트럭 인덱스

        while (idx < truck_weights.length || current > 0) {
            time++;
            // 1. 다리에서 한 칸 빠져나옴
            int left = bridge.poll();
            current -= left; // 빠져나간 게 0일수도 있고, 트럭일 수도 있음.

            // 2. 다음 트럭을 올릴 수 있으면 올리기, 아니면 빈 칸(0) 올리기
            if (idx < truck_weights.length && current + truck_weights[idx] <= weight) {
                bridge.offer(truck_weights[idx]);
                current += truck_weights[idx];
                idx++;
            }
            else {
                bridge.offer(0);
            }
        }
        return time;
    }
}