import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Solution90 {
    class Solution {
        public List<List<Integer>> subsets = new ArrayList<>();
        public List<List<Integer>> subsetsWithDup(int[] nums) {
            Arrays.sort(nums);
            backtrack(nums, new ArrayList<>(), 0);

            return subsets;

        }

        public void backtrack(int[] nums, ArrayList<Integer> list, int start){
            subsets.add(new ArrayList<>(list));
            for (int i = start; i < nums.length; i++){
                if (i > start && nums[i] == nums[i-1]) continue;
                list.add(nums[i]);
                backtrack(nums,list,i+1);
                list.removeLast();
            }
        }
    }

}
