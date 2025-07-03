class Solution {
    public String mergeAlternately(String word1, String word2) {
        String ans = "";


        ans = handler(word1, word2, ans);

        return ans;
    }
    public String handler (String w1, String w2, String ans)
    {
        StringBuilder sb = new StringBuilder(ans);

        if (w1.isEmpty()) {
            sb.append(w2);
            return (sb.toString());
        }

        if (w2.isEmpty()) {
            sb.append(w1);
            return (sb.toString());
        }

        else{
            char fst = w1.toCharArray()[0];
            char snd = w2.toCharArray()[0];
            sb.append(fst);
            sb.append(snd);
        }
        return (handler(w1.substring(1), w2.substring(1), sb.toString()));
    }
}

