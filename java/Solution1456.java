import java.util.Arrays;
import java.util.EnumMap;

public class Solution1456 {
    class Solution {
        public int maxVowels(String s, int k) {
            int maxVowels = 0;
            for (int i = 0 ; i < k; i++){
                if (isVowel(s.charAt(i))){
                    maxVowels++;
                }
            }


            int index = k;
            int numVowels = maxVowels;
            while (index < s.length()){
                if ( isVowel(s.charAt(index)) ){
                    numVowels++;
                }

                if ( isVowel(s.charAt(index-k)) ){
                    numVowels--;
                }

                if (numVowels > maxVowels) maxVowels = numVowels;

                index++;
            }

            return maxVowels;


        }

        public boolean isVowel(char s){
            char[] vowels = new char[]{'a','e','i','o','u'};


            for (char v : vowels){
                if (v == s){
                    return true;
                }
            }

            return false;
        }
    }


    public static void main(String[] args) {
        Solution1456 ss = new Solution1456();
        Solution s = ss.new Solution();

        System.out.println(s.maxVowels("abciiidef",3));
    }
}
