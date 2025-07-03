import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution1207 {

    class Solution {
        public boolean uniqueOccurrences(int[] arr) {


            List<Integer> occurrences = new ArrayList<>();

            Arrays.sort(arr);

            int index = 0;
            int sum = 1;
            while (index < arr.length-1){
                if (arr[index] == arr[index+1]){
                    sum++;
                }else{
                    if (occurrences.contains(sum)){
                        return false;
                    }
                    else{
                        occurrences.add(sum);
                        sum = 1;
                    }
                }

                index++;
            }

            if (occurrences.contains(sum)){
                return false;
            }
            else{
                return true;
            }


        }

    }

    public static void main(String[] args) {
        Solution1207 ss = new Solution1207();
        Solution s = ss.new Solution();

        System.out.println(s.uniqueOccurrences(new int[]{-3,0,1,-3,1,1,1,-3,10,0}));
    }
}
