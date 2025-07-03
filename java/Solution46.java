import java.util.ArrayList;
import java.util.List;

public class Solution46 {
    class Solution{

        List<List<Integer>> permutation = new ArrayList<>();
        public List<List<Integer>> permute(int[] nums){

            backtrack(nums, new ArrayList<Integer>());
            return permutation;
        }


        public void backtrack(int[] nums, ArrayList<Integer> list){
            if (list.size() == nums.length){
                permutation.add(new ArrayList<Integer>(list));
            }

            else {
                for (int i = 0; i < nums.length; i++) {
                    if (list.contains(nums[i])) continue;
                    list.add(nums[i]);
                    backtrack(nums, list);
                    list.removeLast();
                }
            }

        }




    }
}
