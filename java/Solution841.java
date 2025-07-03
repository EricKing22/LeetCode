import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Solution841 {

    class Solution {

        public ArrayList<Integer> keys = new ArrayList<>();

        public boolean canVisitAllRooms(List<List<Integer>> rooms) {
            keys.add(0);
            HashSet<Integer> visited = new HashSet<>(Arrays.asList(0));

            while (!keys.isEmpty() && visited.size() != rooms.size()){
                int room_num = keys.removeFirst();
                for (Integer key : rooms.get(room_num)){
                    if (!visited.contains(key)){
                        keys.add(key);
                        visited.add(key);
                    }
                }
            }

            System.out.println(visited);

            return visited.size() == rooms.size();

        }
    }
}
