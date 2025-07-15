class Solution {
    int count = 0;
    
    public int solution(int[] numbers, int target) {
        backtracking(0, 0, numbers, target);
    
        return count;
    }
    
    public void backtracking(int idx, int currSum, int[] numbers, int target) {
        if (idx == numbers.length) {
            if (currSum == target) count++;
            return;
        }
        
        backtracking(idx + 1, currSum + numbers[idx], numbers, target);
        backtracking(idx + 1, currSum - numbers[idx], numbers, target);
    }
}