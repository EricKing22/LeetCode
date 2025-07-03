import java.util.ArrayList;
import java.util.List;

public class Solution151 {
    public String reverseWords(String s) {
        String[] list = s.trim().split("\\s+");
        String output = "";
        for (String word : reverse(list)){
            output = output + word + " ";
        }

        return output.trim();
    }

    public List<String> reverse(String[] list){
        List<String> output = new ArrayList<>();
        for (int i = list.length-1; i >= 0; i--){
            output.add(list[i]);
        }

        return output;
    }
}
