import java.util.Arrays;
import java.util.Stack;

public class Solution2390 {

    class Solution{
        public String removeStars(String s) {
            Stack<String> stack = new Stack<>();

            String[] list = s.split("");

            for (String l : list){
                if (l.equals("*")){
                    stack.pop();
                }
                else{
                    stack.push(l);
                }
            }


            String answer = "";
            for (String ans : stack){
                answer += ans;
            }

            return answer;
        }



    }

    public static void main(String[] args) {
        Solution2390 ss  = new Solution2390();
        Solution s = ss.new Solution();

        System.out.println(s.removeStars("leet**cod*e"));
    }
}
