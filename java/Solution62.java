import java.util.Arrays;

public class Solution62 {
    class Solution {
        int[][] steps;
        public int uniquePaths(int m, int n) {
            steps = new int[m][n];



            return helper(m,n);



        }

        public int helper(int m, int n){
            for (int i = 0 ; i < m; i++){
                steps[i][0] = 1;
            }

            for (int i = 0 ; i < n; i++){
                steps[0][i] = 1;
            }

            if (m == 1 || n == 1) return steps[m-1][n-1];


            for (int i = 1; i < m; i++){
                for (int j = 1; j < n; j++){
                    steps[i][j] = steps[i-1][j] + steps[i][j-1];
                    System.out.println(steps[i][j]);
                }
            }

            return steps[m-1][n-1];


        }
    }
}
