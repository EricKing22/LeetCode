public class Solution2352 {
    class Solution {
        public int equalPairs(int[][] grid) {

            int count = 0;

            for (int row = 0; row < grid.length; row++){

                for (int column = 0; column < grid.length; column++){
                    boolean match = true;


                    for (int index = 0; index < grid.length; index++) {
                        if (grid[row][index] != grid[index][column]) {
                            match = false;
                            break;
                        }
                    }

                    if(match) {
                        count++;
                    }
                }


            }

            return count;
        }

    }

    public static void main(String[] args) {
        Solution2352 ss = new Solution2352();
        Solution s = ss.new Solution();
        System.out.println(s.equalPairs(new int[][]{{3,2,1},{1,7,6},{2,7,7}}));
    }
}
