import java.util.Arrays;

public class Solution2300 {
    class Solution {
        public int[] successfulPairs(int[] spells, int[] potions, long success) {
            int[] ans = new int[spells.length];
            Arrays.sort(potions);
            for (int i = 0; i < spells.length; i++){
                long spell = spells[i];
                // Binary search

                int mid = 0;
                int high = potions.length-1;
                int low = 0;

                while (low <= high){
                    mid = low + (high - low) / 2;


                    if (potions[mid] * spell >= success)
                        high = mid - 1;

                    if (potions[mid] * spell < success)
                        low = mid + 1;

                }

                ans[i] = potions.length - low;


            }
            return ans;
        }
    }
}
