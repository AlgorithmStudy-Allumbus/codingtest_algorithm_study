import java.util.*;

/*
1. n번쨰 글자를 기준으로 오름차순 정렬.
2. 만약 같은 경우 사전순으로 앞선 문자열이 앞으로 와야 한다.
풀이 시간: 30분
*/
class Solution {
    public String[] solution(String[] strings, int n) {
        // n번쨰 기준으로 정렬하기 전에 전체 정렬
        Arrays.sort(strings);

        // n번째 글자를 기준으로 오름차순 정렬
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                int index = n;
                char c1 = s1.charAt(index);
                char c2 = s2.charAt(index);
                return Character.compare(c1, c2);
            }
        });
        return strings;
    }
}