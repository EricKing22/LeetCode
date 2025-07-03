import java.util.Arrays;

public class Solution746 {
    class Solution {
        int[] minimum;
        public int minCostClimbingStairs(int[] cost) {
            minimum = new int[cost.length+1];
            Arrays.fill(minimum,-1);
            return minCost(cost.length, cost);

        }


        public int minCost(int n, int[] cost){
            if (n < 0) return Integer.MAX_VALUE;
            if (n == 0) return 0;
            if (n == 1) return 0;

            if (minimum[n] != -1){
                return minimum[n];
            }

            minimum[n] = Math.min(cost[n-1] + minCost(n-1, cost), cost[n-2] + minCost(n-2,cost));

            return minimum[n];
        }
    }


}
