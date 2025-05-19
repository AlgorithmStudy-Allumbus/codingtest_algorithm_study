/* 내 풀이 */
import java.util.*;


class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for (int i = 0; i < answer.length; i++) {
            for (int j = i+1; j < answer.length; j++) {
                answer[i] += 1;
                if (prices[i] > prices[j] ) {
                    break;
                }
            }
        }
        return answer;
    }
}

/* 스택 풀이 */
import java.util.Stack;

public class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        // 아직 가격이 떨어지지 않은 시점들의 인덱스를 담을 스택
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < n; i++) {
            // 지금 가격(prices[i])이 스택 위 시점의 가격보다 낮다면,
            // 그 시점의 가격은 i 시점에 떨어진 것이므로
            // answer[idx] = i - idx 로 구간 길이를 확정짓고 pop
            while (!st.isEmpty() && prices[st.peek()] > prices[i]) {
                int idx = st.pop();
                answer[idx] = i - idx;
            }
            // 현재 시점 i를 스택에 추가
            st.push(i);
        }

        // 마지막까지 가격이 떨어지지 않은 인덱스들은
        // 끝까지(마지막 인덱스 n-1) 버틴 시간이 (n-1) - idx
        while (!st.isEmpty()) {
            int idx = st.pop();
            answer[idx] = (n - 1) - idx;
        }

        return answer;
    }
}
