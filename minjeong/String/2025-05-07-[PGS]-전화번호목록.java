import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        
        Arrays.sort(phone_book); // 오름차순 정렬

        for (int i = 0; i < phone_book.length - 1; i++ ) {
		        // 만약 다음 값이 현재 값으로 시작한다면, false 반환
            if (phone_book[i+1].startsWith(phone_book[i])) {
                return false;
            }
        }
        return true;
    }
}