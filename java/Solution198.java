import java.util.Arrays;

public class Solution198 {
    class Solution {
        int[] money;
        public int rob(int[] nums) {
            money = new int[nums.length];
            Arrays.fill(money,-1);

            if (nums.length == 1){
                return nums[0];
            }
            else if (nums.length == 2){
                return Math.max(nums[0], nums[1]);
            }

            return Math.max(rob_n(nums, 0), rob_n(nums,1));

        }

        public int rob_n(int[] nums, int n){
            if (n == nums.length-1){
                money[n] = nums[n];
                return nums[n];
            }

            else if(n == nums.length-2){
                money[n] = nums[n];
                return nums[n];
            }

            else if(n == nums.length-3){
                money[n] = nums[n] + nums[n+2];
                return money[n];
            }

            if (money[n] != -1){
                return money[n];
            }

            money[n] = nums[n] + Math.max(rob_n(nums, n+2), rob_n(nums,n+3));

            return money[n];
        }
    }
}
