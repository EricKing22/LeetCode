import java.awt.desktop.PreferencesEvent;
import java.beans.Introspector;
import java.util.*;

public class Solution1657 {
    class Solution {
        public boolean closeStrings(String word1, String word2) {
            HashMap<String,Integer> set1 = new HashMap();

            for (String s : word1.split("")){
                if (!set1.keySet().contains(s)){
                    set1.put(s,1);
                }
                else{
                    int num = set1.get(s) + 1;
                    set1.put(s,num);
                }
            }

            HashMap<String,Integer> set2 = new HashMap();

            for (String s : word2.split("")){
                if (!set2.keySet().contains(s)){
                    set2.put(s,1);
                }
                else{
                    int num = set2.get(s) + 1;
                    set2.put(s,num);
                }
            }

            if (word1.length() != word2.length()){
                return false;
            }

            for (String s : set1.keySet()){
                if (!set2.containsKey(s)){
                    return false;
                }
            }

            Object[] array1 = set1.values().toArray();
            Object[] array2 = set2.values().toArray();

            Arrays.sort(array1);
            Arrays.sort(array2);

            System.out.println(set1.values());
            System.out.println(set2.values());

            for (int i = 0; i < array1.length; i++) {
                if (!array1[i].equals(array2[i])){
                    return false;
                }
            }

            return true;

        }
    }

    public static void main(String[] args) {
        Solution1657 ss = new Solution1657();
        Solution s = ss.new Solution();

        System.out.println(s.closeStrings("cabbba","abbccc"));
    }




}
