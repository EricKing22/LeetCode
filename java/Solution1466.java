import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution1466 {

    class Solution {

        public int minReorder(int n, int[][] connections) {

            boolean[] visited = new boolean[n];

            ArrayList<ArrayList<Integer>> con = new ArrayList<>();


            for (int i = 0; i < n; i++){
                con.add(new ArrayList<>());
            }

            for (int[] pair : connections){
                con.get(pair[0]).add(pair[1]);
                con.get(pair[1]).add(-pair[0]);
            }

            return backtrack(con, visited, 0);


        }

        public int backtrack(ArrayList<ArrayList<Integer>> con, boolean[] visited, int from){
            int change = 0;
            visited[from] = true;


            for (Integer to : con.get(from)){
                if (visited[Math.abs(to)]) continue;

                change = change + backtrack(con, visited, Math.abs(to)) + (to > 0 ? 1 : 0);
            }

            return change;
        }


    }

}
