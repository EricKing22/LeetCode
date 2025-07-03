import java.util.ArrayList;
import java.util.Arrays;

public class Solution714 {
    class Solution {
        int ans = 0;
        int[] ans_list;

        public int maxProfit(int[] prices, int fee) {
            ans_list = new int[prices.length];
            backtrack(prices, fee, 0, -1, 0);
            return ans;
        }

        public void backtrack(int[] prices, int fee, int index, int sell, int price){
            if (ans_list[index] != 0 && sell == -1){
                price = ans_list[index];
            }

            if (price > ans && sell == -1){
                ans = price;
            }

            if (index == prices.length) return;


            for (int i = index; i < prices.length; i++) {
                int old_price = price;

                price = price + sell * prices[i];
                if (sell == 1){
                    price -= fee;
                    if (price < old_price) return;
                }

                backtrack(prices, fee, i+1, -1 * sell, price);
                price = old_price;

            }


        }
    }
}
