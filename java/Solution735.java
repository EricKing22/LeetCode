import java.util.Arrays;

public class Solution735 {
    class Solution{
        public int[] asteroidCollision(int[] asteroids) {
            boolean noCollision = false;

            while(!noCollision) {
                noCollision = true;
                for (int i = 0; i < asteroids.length - 1; i++) {

                    if (asteroids[i] >= 0 && asteroids[i + 1] <= 0) { // different direction
                        int a = Math.abs(asteroids[i]);
                        int b = Math.abs(asteroids[i + 1]);
                        noCollision = false;

                        if (a > b) {
                            int[] newList = new int[asteroids.length - 1];
                            for (int j = 0; j < newList.length; j++) {
                                if (j < i + 1) {
                                    newList[j] = asteroids[j];
                                } else {
                                    newList[j] = asteroids[j + 1];
                                }
                            }


                            return asteroidCollision(newList);


                        } else if (a < b) {

                            int[] newList = new int[asteroids.length - 1];
                            for (int j = 0; j < newList.length; j++) {
                                if (j < i) {
                                    newList[j] = asteroids[j];
                                } else {
                                    newList[j] = asteroids[j + 1];
                                }
                            }

                            return asteroidCollision(newList);
                        } else {

                            int[] newList = new int[asteroids.length - 2];
                            for (int j = 0; j < newList.length; j++) {
                                if (j < i) {
                                    newList[j] = asteroids[j];
                                } else {
                                    newList[j] = asteroids[j + 2];
                                }
                            }

                            return asteroidCollision(newList);

                        }
                    }
                }
            }

            return asteroids;
        }
    }

    public static void main(String[] args) {

        Solution735 ss = new Solution735();
        Solution s = ss.new Solution();


        System.out.println( Arrays.toString(s.asteroidCollision(new int[] {10,2,-5})) );

    }
}
