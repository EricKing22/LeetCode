import java.util.Arrays;

public class Solution875 {
    class Solution {
        public int minEatingSpeed(int[] piles, int h) {

            Arrays.sort(piles);

            long left = piles[0];
            long mid = 0;
            long right = piles[piles.length-1];

            while (left <= right){
                mid = left + (right - left) / 2;

                long time = 0;

                for (long pile : piles){
                    time += (pile + mid - 1) / mid;
                }


                if (time > h){
                    left = mid + 1;
                }
                else{
                    right = mid - 1;
                }

            }

            return (int) left;
        }
    }
}
