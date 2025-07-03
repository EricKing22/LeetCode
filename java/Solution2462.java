import java.util.PriorityQueue;

public class Solution2462 {
    class Solution {
        public long totalCost(int[] costs, int k, int candidates) {
            int i = 0;
            int j = costs.length - 1;

            PriorityQueue<Integer> first = new PriorityQueue<>();
            PriorityQueue<Integer> second = new PriorityQueue<>();

            long total_cost = 0;


            while (k > 0){
                while (first.size() < candidates && i <= j){
                    first.add(costs[i]);
                    i++;
                }

                while (second.size() < candidates && i <= j){
                    second.add(costs[j]);
                    j--;
                }

                Integer a = Integer.MAX_VALUE;
                if (!first.isEmpty()) a = first.peek();

                Integer b = Integer.MAX_VALUE;
                if (!second.isEmpty()) b = second.peek();

                int cost = 0;

                if (a < b){
                    cost = first.poll();
                }
                else {
                    cost = second.poll();
                }

                total_cost += cost;

                k--;

            }

            return total_cost;
        }
    }
}
