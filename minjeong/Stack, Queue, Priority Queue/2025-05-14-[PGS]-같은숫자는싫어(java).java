import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();

        // 1. 첫 번째 값은 무조건 추가
        answer.add(arr[0]);

        // 2. 두 번째 값부터 순차적으로 확인
        for (int i = 1; i < arr.length; i++) {
		        // 바로 이전 값과 다르면 추가
            if (answer.get(answer.size()-1) != arr[i]) {
                answer.add(arr[i]);
            }
        }

        // 3. ArrayList → int[] 변환
        int[] answer2 = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++){
            answer2[i] = answer.get(i);
        }
        return answer2;
    }
}