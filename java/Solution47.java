
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution47 {
    class Solution{

        List<List<Integer>> permutation = new ArrayList<>();



        public List<List<Integer>> permuteUnique(int[] nums) {

            Arrays.sort(nums);
            boolean[] used = new boolean[nums.length];
            backtrack(nums, used, new ArrayList<>());
            return permutation;
        }



        public void backtrack(int nums[], boolean[] used, ArrayList<Integer> list){
            if (list.size() == nums.length ){
                permutation.add(new ArrayList<>(list));

            }

            for (int i = 0; i < nums.length; i++){
                if (used[i] || (i != 0 && nums[i] == nums[i-1] && !used[i-1])){
                    continue;
                }

                else {
                    used[i] = true;
                    list.add(nums[i]);
                    backtrack(nums, used, list);
                    list.removeLast();
                    used[i] = false;
                }
            }
        }


        public int count(int[] nums, int n){
            int count = 0;
            for (int num : nums){
                if (num == n) count++;
            }
            return count;
        }

        public int count(List<Integer> nums, int n){
            int count = 0;
            for (int num : nums){
                if (num == n) count++;
            }
            return count;
        }

    }


}
