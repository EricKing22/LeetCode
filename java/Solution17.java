import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution17 {
    class Solution {
        List<String> list = new ArrayList<>();
        HashMap<String, String> dict = new HashMap<>();



        public List<String> letterCombinations(String digits) {
            dict.put("2","abc");
            dict.put("3","def");
            dict.put("4","ghi");
            dict.put("5","jkl");
            dict.put("6","mno");
            dict.put("7","pqrs");
            dict.put("8","tuv");
            dict.put("9","wxyz");

            if (digits == null || digits.isEmpty()){
                return list;
            }


            backtrack(digits, new StringBuilder(), 0);


            return list;


        }

        public void backtrack(String digits, StringBuilder temp, int start){
            if (temp.length() == digits.length()){
                list.add(temp.toString());
                return;
            }

            String letters = dict.get(digits.substring(start,start+1));


            for (char letter : letters.toCharArray()){
                temp.append(letter);
                backtrack(digits, temp, start+1);
                temp.deleteCharAt(temp.length()-1);
            }

        }


    }
}
