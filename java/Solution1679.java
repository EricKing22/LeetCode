import java.util.ArrayList;
import java.util.Arrays;

public class Solution1679 {

    class Solution {
        public int maxOperations(int[] nums, int k){
            Arrays.sort(nums);

            int i = 0;
            int j = nums.length-1;
            int count = 0;

            while(i < j){
                int sum = nums[i] + nums[j];
                if (sum == k){
                    count++;
                    i++;
                    j--;
                }
                else if (sum < k){
                    i++;
                }
                else{
                    j--;
                }
            }

            return count;



        }
    }

    class Solution1 {
        public int maxOperations(int[] nums, int k){
            int ans = 0;

            if (nums.length == 0) return 0;

            int i = nums[0];
            for (int j : tail(nums)){
                if (i+j == k){
                    return (1 + maxOperations(remove2(i,j,nums) ,k));
                }
            }
            return maxOperations(tail(nums),k);



        }

        public int[] remove2(int a, int b, int[] array){
            int[] newArray = new int[array.length-2];
            int newIndex = 0;
            boolean removedNum1 = false;
            boolean removedNum2 = false;

            for (int i = 0; i < array.length; i++){
                if (!removedNum1 && array[i] == a){
                    removedNum1 = true;
                }
                else if(!removedNum2 && array[i] == b){
                    removedNum2 = true;
                }
                else {
                    newArray[newIndex++] = array[i];
                }
            }

            return newArray;
        }

        public int[] tail(int[] array){
            int[] newArray = new int[array.length-1];
            for(int i = 1; i < array.length; i++){
                newArray[i-1] = array[i];
            }

            return newArray;
        }
    }

    public static void main(String[] args) {
        Solution1679 ss = new Solution1679();
        Solution s = ss.new Solution();
        System.out.println(s.maxOperations(new int[]{1,2,3,4,5}, 5));
        System.out.println(s.maxOperations(new int[]{3,1,3,4,3}, 6));
    }
}
