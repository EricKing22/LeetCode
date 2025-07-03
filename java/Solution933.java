import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution933 {

    class RecentCounter {

        Queue<Integer> q = new LinkedList<>();
        public RecentCounter() {

        }

        public int ping(int t) {
            q.add(t);

            int s = t-3000;

            while(q.peek() < s)
            {
                q.poll(); // q.remove()
            }

            return q.size();
        }
    }

    class RecentCounter1 {
        int counter;

        ArrayList<Integer> requests = new ArrayList<>();

        public RecentCounter1(){
            counter = 0;
        }

        public int ping(int t) {
            counter = 0;
            requests.add(t);

            int left;
            if (t - 3000 < 0){
                left = 0;
            }
            else {
                left = t - 3000;
            }

            int right = t;

            for (int i : requests){
                if (i >= left && i <= right){
                    counter++;
                }
            }

            return counter;
        }
    }
}
