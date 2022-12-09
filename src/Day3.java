import java.util.Arrays;
import java.util.List;

public class Day3 {

    public static int getGroupScore(List<String> allLines) {

        boolean[] buckets = new boolean[52];
        boolean[] filter = new boolean[52];
        Arrays.fill(buckets, true);
        int counter = 0, score = 0;

        for(String line : allLines) {


            for(int i=0; i<line.length(); i++)
                filter[getValue(line, i) - 1] = true;

            for(int i=0; i<52; i++) {
                buckets[i] = buckets[i] && filter[i];
            }

            if(++counter == 3) {
                for(int i = 0; i<buckets.length; i++)
                    if(buckets[i])
                        score += i + 1;


                Arrays.fill(buckets, true);
                counter = 0;
            }

            Arrays.fill(filter, false);

        }

        return score;

    }

    public static int getScore(List<String> allLines) {
        boolean[] buckets;
        int score = 0;

        for(String line : allLines) {
            buckets = new boolean[52];

            for (int i = 0; i < line.length() / 2; i++)
                buckets[getValue(line, i) - 1] = true;

            for (int i = line.length() / 2; i < line.length(); i++) {
                int val = getValue(line, i);
                if (buckets[val - 1]) {
                    score += val;
                    break;
                }
            }
        }

        return score;
    }

    public static int getValue(String line, int i) {
        int val = line.charAt(i);
        if(val > 96 && val < 123)
            return val - 96;
        return val - 38;
    }

}
