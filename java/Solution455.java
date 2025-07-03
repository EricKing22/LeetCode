import java.util.Arrays;

public class Solution455 {
    public int findContentChildren(int[] g, int[] s) {
        int num = 0;

        Arrays.sort(g);
        Arrays.sort(s);

        for (int i : g){
            for (int j = 0; j < s.length; j++){
                if (i <= s[j]){
                    num++;
                    s[j] = 0;
                    break;
                }
            }
        }

        return num;


    }


}
