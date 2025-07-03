import java.sql.SQLOutput;
import java.util.*;

public class Solution994 {

    class Solution {
        Queue<int[]> rotten_list = new LinkedList<>();
        int fresh_num = 0;

        public int orangesRotting(int[][] grid) {
            int new_fresh_num = 0;
            for (int i = 0; i < grid.length; i++){
                for (int j = 0; j < grid[0].length; j++){
                    if (grid[i][j] == 1) new_fresh_num++;
                    else if (grid[i][j] == 2) rotten_list.add(new int[]{i,j});
                }
            }
            int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};


            int steps = 0;



            while (new_fresh_num != fresh_num){
                steps++;
                fresh_num = new_fresh_num;


                int n = rotten_list.size();
                for (int i = 0; i < n; i++){
                    int[] node = rotten_list.poll();

                    for (int[] direction : directions){
                         int x = node[0] + direction[0];
                         int y = node[1] + direction[1];

                         if (x < 0 || x > grid.length-1 || y < 0 || y > grid[0].length-1) continue;

                         if (grid[x][y] == 1) {
                             grid[x][y] = 2;
                             new_fresh_num--;
                             rotten_list.add(new int[]{x, y});
                         }

                    }

                }

                if (fresh_num == new_fresh_num) steps--;

            }


            return fresh_num == 0 ? steps : -1;


        }
    }
}
