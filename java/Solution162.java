public class Solution162 {
    class Solution {
        public int findPeakElement(int[] nums) {
            if (nums.length == 1) return 0;
            int last = nums.length-1;
            int first = 0;


            if (nums[0] > nums[1]) return 0;
            if (nums[last] > nums[last-1]) return last;

            first++;
            last--;


            int mid = first + (last - first) / 2;

            while (first <= last){
                if (nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1]) return mid;

                else if (nums[mid] < nums[mid-1]) last = mid - 1;
                else if (nums[mid] < nums[mid+1]) first = mid + 1;
            }
            return -1;
        }
    }
}
