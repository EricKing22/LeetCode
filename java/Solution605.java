import java.util.ArrayList;
import java.util.List;

public class Solution605 {

        public boolean canPlaceFlowers(int[] flowerbed, int n){

            for (int i = 0; i < flowerbed.length; i++) {

                if (flowerbed[i] == 0) {
                    boolean emptyLeft = (i == 0 || flowerbed[i - 1] == 0);
                    boolean emptyRight = (i == flowerbed.length - 1 || flowerbed[i + 1] == 0);

                    if (emptyRight && emptyLeft) {
                        flowerbed[i] = 1;
                        n--;

                        if (n == 0) return true;
                    }
                }

            }

            return n <= 0;


        }
    public boolean canPlaceFlowers1(int[] flowerbed, int n) {
        List<Integer> possible_pos = new ArrayList<>();


        for (int i = 0; i < flowerbed.length; i++){

            try {


                int current = flowerbed[i];
                int previous = flowerbed[i-1];
                int next = flowerbed[i+1];


                if (current == 0){
                    if (previous != 1 && next != 1){
                        possible_pos.add(i);
                        flowerbed[i] = 1;
                    }
                }

            }
            catch (IndexOutOfBoundsException e){
                if (flowerbed[i] == 0) {
                    int next = 1;
                    try {
                        if (i == 0) {
                            next = flowerbed[i + 1];
                        } else {
                            next = flowerbed[i - 1];
                        }
                    }
                    catch (IndexOutOfBoundsException w){
                        next = 0;
                    }

                    if (next == 0) {
                        possible_pos.add(i);
                        flowerbed[i] = 1;
                    }
                }
            }

        }

        System.out.println(possible_pos.size());

        return (possible_pos.size() >= n);
    }


    public static void main(String[] args){
        new Solution605().canPlaceFlowers(new int[] {0,0,1,0,0}, 1);

    }
}
