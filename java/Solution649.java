import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Solution649 {

    class Solution {
        public String predictPartyVictory(String senate) {

            LinkedList<String> queue = new LinkedList();

            for (String s : senate.split("")){
                queue.add(s);
            }

            boolean removed = true;

            while (true) {
                String current = queue.pop();

                if (current.equals("R")) {

                    queue.add(current);

                    if (!queue.removeFirstOccurrence("D")){
                        return "Radiant";
                    }
                }
                else {
                    queue.add(current);

                    if (!queue.removeFirstOccurrence("R")){
                        return "Dire";
                    }


                }
            }


        }
    }
}
