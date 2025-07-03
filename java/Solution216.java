import java.util.ArrayList;
import java.util.List;

public class Solution216 {
    class Solution {
        List<List<Integer>> list = new ArrayList<>();
        int[] numbers = new int[9];

        public List<List<Integer>> combinationSum3(int k, int n) {

            for (int i = 0; i < numbers.length; i++){
                numbers[i] = i + 1;
            }

            backtrack(k,n,new ArrayList<>(), 0);

            return list;
        }

        public void backtrack(int k, int n, ArrayList<Integer> temp, int start){
            int sum = sum(temp);

            if (sum > n || temp.size() > k) return;

            if (temp.size() == k && sum == n){
                list.add(new ArrayList<>(temp));
                return;
            }

            for (int i = start; i < numbers.length; i++){
                temp.add(numbers[i]);
                backtrack(k, n, temp, i+1);
                temp.removeLast();
            }

        }

        public int sum(List<Integer> list){
            int ans = 0;

            for (Integer i : list){
                ans += i;
            }

            return ans;
        }
    }
}
