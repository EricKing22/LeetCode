public class Solution724 {
    class Solution {

        public int pivotIndex(int[] nums){

            int sum = 0;
            for (int n : nums){
                sum += n;
            }

            int left = 0;
            int right = sum;

            for (int i = 0; i < nums.length; i++){

                right = sum - left - nums[i];

                if (left == right) return i;

                left += nums[i];
            }


            return -1;


        }
        public int pivotIndex1(int[] nums){


            for (int i = 0; i < nums.length; i++){
                int leftSum = 0;
                for (int j = 0; j < i; j++){
                    leftSum += nums[j];
                }
                int rightSum = 0;
                for (int j = i+1; j < nums.length; j++){
                    rightSum += nums[j];
                }

                if (leftSum == rightSum) return i;

            }

            return -1;
        }

    }

    public static void main(String[] args) {
        Solution724 ss = new Solution724();
        Solution s = ss.new Solution();

        System.out.println(s.pivotIndex(new int[]{1,7,3,6,5,6}));
    }

}
