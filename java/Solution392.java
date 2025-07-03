public class Solution392 {


    class Solution {
        public boolean isSubsequence(String s, String t){
            if (s.equals("")){
                return true;
            }

            else if (s.length() > t.length()) {
                return false;
            }

            else if (s.charAt(0) == t.charAt(0)) {
                return isSubsequence(s.substring(1), t.substring(1));
            }

            else if (s.length() < t.length()) {
                return isSubsequence(s, t.substring(1));
            }

            return false;


        }
    }


    public static void main(String[] args) {
        Solution392 ss = new Solution392();
        Solution s = ss.new Solution();
        System.out.println(s.isSubsequence("axc","ahbgdc"));
    }
}
