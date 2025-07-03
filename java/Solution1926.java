import java.util.*;

public class Solution1926 {
    class Solution {
        Queue<List<Integer>> nodes = new LinkedList<>();


        public int nearestExit(char[][] maze, int[] entrance) {


            int[][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};

            nodes.add(Arrays.asList(entrance[0],entrance[1]));
            maze[entrance[0]][entrance[1]] = '+';

            int steps = 0;

            while (!nodes.isEmpty()){

                steps++;
                int n = nodes.size();
                for (int i = 0; i < n; i++){

                    List<Integer> node = nodes.poll();

                    for (int[] direction : directions){
                        Integer x = node.getFirst() + direction[0];
                        Integer y = node.getLast() + direction[1];


                        if (x < 0 || y < 0 || x > maze.length - 1 || y > maze[0].length - 1 ) continue;

                        if (maze[x][y] == '+') continue;

                        if (x == 0 || y == 0 || x == maze.length - 1 || y == maze[0].length - 1){
                            return steps;
                        }

                        maze[x][y] = '+';

                        nodes.add(Arrays.asList(x,y));
                    }
                }


            }

            return -1;

        }

    }



}
