import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution215 {
    class Solution {
        public int findKthLargest(int[] nums, int k) {
            PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    if (o1 < o2) return 1;
                    if (o1 > o2) return -1;
                    return 0;
                }
            });

            for (int n : nums){
                pq.add(n);
            }



            for (int i = 0; i < k-1; i++){
                pq.poll();
            }

            return pq.poll();
        }
    }
}
