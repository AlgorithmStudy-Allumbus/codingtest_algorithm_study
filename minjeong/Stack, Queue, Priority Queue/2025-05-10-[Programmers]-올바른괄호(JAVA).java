import java.util.*;

class Solution {
    boolean solution(String s) {
        // "(" 이면 stack에 push. ")"이면 stack에서 pop하기
        // stack의 길이가 0이면 true, stack의 길이가 1이상이면 false

        // Stack ArrayList
        ArrayList<Integer> stack = new ArrayList<>();

        // 문자열을 ArrayList로 변환
        String[] stringParam = s.split("");
        ArrayList<String> list = new ArrayList<String>(Arrays.asList(stringParam));

        // Stack Push & Pop
        for (String str: stringParam){
            // System.out.println(str);
            if (str.equals("(")) {
                stack.add(0);
                // System.out.println("추가 완료");
            }
            else {
		            // 처음부터 ) 가 나올 경우 올바르지 않은 괄호
                if (stack.size() == 0){
                    return false;
                }
                else {
                    stack.remove(stack.size() - 1);
                }
            }
        }

        // 올바른 괄호가 아닐 경우
        if (stack.size() > 0) {
            return false;
        }
        // 올바른 괄호가 아닌 경우
        return true;
    }
}