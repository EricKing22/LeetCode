import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution547 {

    class Solution{

        List<Integer> tempList = new ArrayList<>();

        public int findCircleNum(int[][] isConnected) {
            boolean[] visited = new boolean[isConnected.length];
            HashMap<Integer, List<Integer>> dict = new HashMap<>();

            int count = 0;

            for (int i = 0; i < isConnected.length; i++){


                backtrack(isConnected, i, visited);

                if (!tempList.isEmpty()){
                    dict.put(count, new ArrayList<Integer>(tempList));
                    tempList.clear();
                    count++;
                }

            }
            System.out.println(dict);
            return dict.size();

        }


        public void backtrack(int[][] isConnected, int index, boolean[] visited){
            for (int i = 0; i < isConnected[index].length; i++){
                if (visited[i] || isConnected[index][i] != 1) continue;

                tempList.add(i);
                visited[i] = true;
                backtrack(isConnected, i, visited);


            }
        }


    }
}
