import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Arrays.sort(scoville);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        // scoville 배열을 minHeap으로 옮기기
        for (int s: scoville) {
            minHeap.offer(s);
        }
        
        // minHeap의 크기가 1보다 작아질 때까지 반복
        while (minHeap.size() > 1) {
		        // 이미 K보다 크다면 바로 return
            if (minHeap.peek() >= K) {
                return answer;
            }
            int a = minHeap.poll();
            int b = minHeap.poll();
            minHeap.offer(a + b * 2);
            answer++;
        }
        
        // 마지막 하나도 확인해야 한다.
        if (minHeap.peek() >= K) {
            return answer;
        }
       
        return -1;
    }
}