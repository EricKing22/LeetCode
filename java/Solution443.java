public class Solution443 {

    static class Solution {
        String out = "";
        public int compress(char[] chars) {
            for (int i = 0; i < chars.length; i++){
                String currentChar = Character.toString(chars[i]);
                int count = 1;

                if (i != chars.length-1) {
                    while (Character.toString(chars[i + 1]).equals(currentChar)) {
                        count++;
                        i++;
                        if (i == chars.length - 1) break;
                    }
                }
                if (count == 1){
                    out = out + currentChar;
                }
                else {
                    out = out + currentChar + count;
                }
            }

            for (int i = 0; i < out.length(); i++){
                chars[i] = out.charAt(i);
            }

            return out.length();
        }
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        char[] chars = {'a','a','b','b','c','c','c','d'};
        System.out.println(solution.compress(chars));
    }
}
