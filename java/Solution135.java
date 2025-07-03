import java.util.Arrays;

public class Solution135 {
    class Solution {
        public int candy(int[] ratings) {

            ratings = new int[]{1,0,2};

            int[] candy = new int[ratings.length];

            for (int i = 0; i < candy.length; i++){
                candy[i] = 1;
            }

            for (int i = 0; i < ratings.length-1; i++){
                if (ratings[i+1] > ratings[i]){
                    candy[i+1] = candy[i] + 1;
                }
            }

            for (int i = ratings.length-1; i > 0; i--){
                if (ratings[i-1] > ratings[i] && candy[i-1] <= candy[i]){
                    candy[i-1] = candy[i] + 1;
                }
            };


            return Arrays.stream(candy).sum();

        }


    }

}
