public class Solution334 {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num <= first) {
                first = num;
            } else if (num <= second && num > first) {
                second = num;
            } else if (num >= second && num >= first) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args){
        int[] t = new int[]{1,2,0};
        System.out.println(new Solution334().increasingTriplet(t));
    }

}
