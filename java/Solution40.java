import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution40 {
    class Solution{

        List<List<Integer>> result = new ArrayList<>();
        public List<List<Integer>> combinationSum2(int[] candidates, int target) {


            Arrays.sort(candidates);

            boolean[] used = new boolean[candidates.length];
            backtrack(candidates, used, new ArrayList<Integer>(), target, 0);

            return result;

        }

        public void backtrack(int[] candidates, boolean[] used, ArrayList<Integer> list, int remain, int start){

            if (remain < 0) return;
            if (remain == 0) result.add(new ArrayList<>(list));

            else{
                for (int i = start; i < candidates.length; i++){
                    if (count(candidates, candidates[i]) == count(list, candidates[i])){
                        continue;
                    }

                    if (used[i] || (i != 0 && candidates[i] == candidates[i-1]) && !used[i-1]){
                        continue;
                    }


                    else {
                        used[i] = true;
                        list.add(candidates[i]);
                        backtrack(candidates,used, list, remain - candidates[i], i+1);
                        list.removeLast();
                        used[i] = false;
                    }
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
