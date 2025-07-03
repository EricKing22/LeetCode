import java.util.*;

public class Solution2542 {
    class Solution {

        List<Integer> nums1 = new ArrayList<>();
        List<Integer> nums2 = new ArrayList<>();
        long ans = 0;

        public long maxScore(int[] nums1, int[] nums2, int k) {
            backtrack(nums1,nums2,k,0);

            return ans;
        }

        public void backtrack(int[] nums1, int[] nums2, int k, int start){
            if (this.nums1.size() == k && this.nums2.size() == k){
                long sum = 0;
                for (int num : this.nums1){
                    sum += num;
                }

                long min = Long.MAX_VALUE;
                for (int num : this.nums2){
                    if (num < min) min = num;
                }
                if (sum * min > ans){
                    ans = sum * min;
                }

            }

            for (int i = start; i < nums1.length; i++){
                this.nums1.add(nums1[i]);
                this.nums2.add(nums2[i]);
                backtrack(nums1,nums2,k,i+1);
                this.nums1.removeLast();
                this.nums2.removeLast();
            }


        }



    }

}
