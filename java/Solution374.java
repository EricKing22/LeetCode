public class Solution374 {
    public class Solution extends GuessGame {
        // Binary search
        public int guessNumber(int n) {

            int mid = 0;
            int high = n;
            int low = 0;


            while(low < high){
                mid = low + (high - low) / 2;
                int ans = guess(mid);
                if (ans == 0) return mid;
                if (ans == -1) high = mid - 1;
                if (ans == 1) low = mid + 1;
            }

            return -1;



        }
    }
}
