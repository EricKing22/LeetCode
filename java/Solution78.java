import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution78 {
    class Solution{
        public List<List<Integer>> subsets = new ArrayList<>(new ArrayList<>());

        public List<List<Integer>> subsets(int[] nums) {
            backtrack(nums, new ArrayList<>(), 0);
            return subsets;
        }

        public void backtrack(int[] nums, ArrayList<Integer> list, int start){
            subsets.add(new ArrayList<>(list));
            for (int i = start; i < nums.length; i++){
                list.add(nums[i]);
                backtrack(nums, list, i+1);
                list.removeLast();
            }

        }
    }
}
