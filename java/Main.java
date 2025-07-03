
import java.util.Scanner;
import java.util.ArrayList;
class SS{
    public static void main(String args[]) {
        try (Scanner scanner = new Scanner(args[0])) {

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] list = line.split("");

                ArrayList<Integer> dot_positions = new ArrayList<>();

                for (int i = 0; i < line.length(); i++) {
                    if (list[i].equals(".")) {
                        dot_positions.add(i);
                    }
                }

                int long_distance = line.length();
                int short_distance = 0;

                for (int i : dot_positions) {

                    for (int j = i; j < line.length(); j++) {
                        if (list[j].equals("X")) {
                            long_distance = j - i - 1;
                            break;
                        }
                    }

                    for (int j = i; j >= 0; j--) {
                        if (list[j].equals("X") && i - j - 1 < long_distance) {
                            long_distance = i - j - 1;
                            break;
                        }
                    }

                    if (long_distance > short_distance) {
                        short_distance = long_distance;
                    }
                }

                System.out.println(short_distance);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

