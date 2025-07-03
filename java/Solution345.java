import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

public class Solution345 {
    //Reverse Vowels of a String
    char[] vowels = new char[] {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'};

    public String reverseVowels(String input) {
        List<Character> allVowels = new ArrayList<Character>();

        for (char s : input.toCharArray()){
            if (contains(s)){
                allVowels.add(s);
            }
        }

        Collections.reverse(allVowels);

        int index = 0;
        StringBuilder output = new StringBuilder();

        for (char s : input.toCharArray()){
            if (contains(s)){
                output.append(allVowels.get(index));
                index += 1;
            }
            else {
                output.append(s);
            }
        }

        return output.toString();
    }

    public Boolean contains(char c){
        for (char v : vowels){
            if (v == c){
                return true;
            }
        }
        return false;
    }
}