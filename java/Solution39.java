import java.util.*;

public class Solution39 {
    class Solution {

        public List<List<Integer>> list = new ArrayList<>();


        public List<List<Integer>> combinationSum(int[] candidates, int target) {
            Arrays.sort(candidates);
            backtrack(new ArrayList<>(),candidates,target,0);
            return list;
        }



        public void backtrack (List<Integer> temp, int[] nums, int remain, int start){
            if (remain < 0) return;
            else if (remain == 0) list.add(new ArrayList<>(temp));

            else{
                for (int i = start; i < nums.length; i++){
                    temp.add(nums[i]);
                    backtrack(temp, nums,remain-nums[i],i);
                    temp.removeLast();
                }

            }
        }

    }
}
