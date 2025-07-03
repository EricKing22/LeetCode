import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution2215 {

    class Solution {
        public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
            List<List<Integer>> list = new ArrayList<>();

            List<Integer> l1 = new ArrayList<>();
            List<Integer> l2 = new ArrayList<>();

            list.add(l1);
            list.add(l2);

            for (int n1 : nums1){
                if (!list.get(0).contains(n1)) {
                    list.get(0).add(n1);
                }
            }

            for (int n2 : nums2){
                if (!list.get(1).contains(n2)) {
                    list.get(1).add(n2);
                }
                list.get(0).remove(Integer.valueOf(n2));
            }

            for (int n1 : nums1){
                list.get(1).remove(Integer.valueOf(n1));
            }

            return list;

        }
    }


    public static void main(String[] args) {
        Solution2215 ss = new Solution2215();
        Solution s = ss.new Solution();


        System.out.println(s.findDifference(new int[]{1,2,3,3}, new int[]{1,1,2,2}));
    }
}
