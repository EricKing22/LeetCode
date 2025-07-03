public class Solution1004 {
    class Solution {
        public int longestOnes(int[] nums, int k) {
            int left = 0;
            int right = 0;
            int zeros = 0;
            while (right < nums.length){
                if (nums[right] == 0){
                    zeros++;
                }

                right++;

               if (zeros > k){
                   if(nums[left] == 0){
                       zeros--;
                   }

                   left++;

               }
            }

            return right-left;
        }

    }

    public static void main(String[] args) {
        Solution1004 ss = new Solution1004();
        Solution s = ss.new Solution();

        System.out.println(s.longestOnes(new int[]{0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1},3));
    }
}
