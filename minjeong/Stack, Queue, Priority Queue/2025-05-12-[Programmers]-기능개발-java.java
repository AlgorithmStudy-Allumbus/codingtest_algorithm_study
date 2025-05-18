import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<Integer> queue = new ArrayList<>();

        for (int i=0; i < progresses.length; i++){
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            if (queue.size() > 0 && days > queue.get(0)) {
                answer.add(queue.size());
                queue.clear();
                queue.add(days);

            }
            else {
                queue.add(days);
            }
        }
        answer.add(queue.size());

        // 배열로 변환
        int[] arr = answer.stream()
                  .mapToInt(Integer::intValue)
                  .toArray();

        return arr;
    }
}