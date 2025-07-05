import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int boat = 0;
        int left = 0;
        int right = people.length - 1;

        Arrays.sort(people);

        while (left <= right) {
            if (people[left] + people[right] <= limit) {
                left += 1;
                right -= 1;
            } else {
                right -= 1;
            }
            boat += 1;

        }
        return boat;
    }
}