import java.util.ArrayList;

public class Solution283 {

    static class Solution {

        public int[] moveZeros (int[] chars){
            int count = 0;

            // use count to track the last position
            for (int i = 0; i < chars.length; i++){
                if (chars[i] != 0){
                    chars[count] = chars[i];
                }
                count++;
            }

            for (int i = count; i < chars.length; i++){
                chars[i] = 0;
            }

            return chars;

        }

        public int[] moveZeroes1(int[] nums) {
            boolean change = true;
            int length = nums.length-1;
            while (change) {
                change = false;
                for (int i = 0; i < length; i++) {
                    if (nums[i] == 0) {
                        change = true;
                        int temp = nums[i + 1];
                        nums[i] = temp;
                        nums[i + 1] = 0;
                    }
                }
                length--;
            }

            for (int n : nums) System.out.println(n);
            return nums;
        }

        public void moveZeroes(int[] nums) {
            int n = nums.length;
            int i =0;
            for (int j =0;j<n;j++)
            {
                if(nums[j] != 0)
                {
                    nums[i] = nums[j];
                    i++;
                }
            }
            for(int k = i ; k<n ;k++)
            {
                nums[k] = 0;
            }
        }
    }



    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.moveZeroes( new int[] {0,1,0,3,12} );
    }
}
