public class Solution643 {
    class Solution {
        public double findMaxAverage(int[] nums, int k) {


            double sum = 0;
            for (int i = 0 ; i < k; i++){
                sum += nums[i];
            }

            double maxSum = sum;

            int index = k;

            while (index < nums.length){
                sum += nums[index] - nums[index-k];

                if (sum > maxSum) maxSum = sum;
                index++;
            }

            return (double) maxSum / k;
        }

    }

    public static void main(String[] args) {
        Solution643 ss = new Solution643();
        Solution s = ss.new Solution();
        System.out.println(s.findMaxAverage(new int[]{1,12,-5,-6,50,3}, 4));
    }
}
