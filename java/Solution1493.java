import javax.sound.midi.Soundbank;

public class Solution1493 {
    class Solution {
        public int longestSubarray(int[] nums) {
            int left = 0;
            int right = 0;
            int zeros = 0;

            while (right < nums.length){
                if (nums[right] == 0){
                    zeros++;
                }

                right++;

                if (zeros > 1){
                    if(nums[left] == 0){
                        zeros--;
                    }

                    left++;

                }
            }

            return right-left-1;
        }


    }

    public static void main(String[] args) {

        Solution1493 ss = new Solution1493();
        Solution s = ss.new Solution();
        System.out.println(s.longestSubarray(new int[]{1,1,1}));
    }
}
