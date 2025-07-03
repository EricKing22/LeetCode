import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution1431 {


    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        List<Boolean> ans = new ArrayList<>();


        int max = 0;

        for (int i : candies){
            if (i > max) max = i;
        }

        for (int i : candies){
            if (i + extraCandies >= max) {
                ans.add(true);
            }
            else {
                ans.add(false);
            }
        }

        return ans;

    }

    public List<Boolean> kidsWithCandies1(int[] candies, int extraCandies) {

        List<Boolean> ans = new ArrayList<Boolean>();
        for (int candy : candies){
            ans.add(isGreatest(candy+extraCandies, candies));
        }

        return ans;
    }

    public boolean isGreatest (int num, int[] list){
        for (int i : list){
            if (num < i){
                return false;
            }
        }

        return true;
    }
}
