// 풀이 1: 정렬을 이용한 풀이
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        for (int i = 0; i < completion.length; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }

        return participant[participant.length - 1];
    }
}

// 풀이2: 해시맵을 이용한 풀이
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";

        HashMap<String, Integer> dict = new HashMap<>();

        for (String p : participant) dict.put(p, dict.getOrDefault(p, 0) + 1);
        for (String c : completion) dict.put(c, dict.get(c) - 1);

        for (String key: dict.keySet()) {
            if (dict.get(key) != 0) {
                answer = key;
            }
		}

        return answer;
    }
}