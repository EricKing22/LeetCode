import java.util.PriorityQueue;

public class Solution2336 {
    class SmallestInfiniteSet {

        PriorityQueue<Integer> pq;
        int n = 1;

        public SmallestInfiniteSet() {
            pq = new PriorityQueue();
            pq.add(n);

        }

        public int popSmallest() {
            n++;
            if (!pq.contains(n)) pq.add(n);
            return pq.poll();

        }

        public void addBack(int num) {
            if (!pq.contains(num)) pq.add(num);
        }
    }
}
