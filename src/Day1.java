import java.util.List;

public class Day1 {

    private static int get3Max(List<String> allLines) {
        int[] max = {0, 0, 0};
        int ret = 0, cur = 0;

        for (String line : allLines) {
            if(line.equals("")) {
                if(cur > max[0]) {
                    max[0] = cur;

                    for(int i = 0; i<max.length-1; i++) {
                        if(max[i] > max[i+1]) {
                            cur = max[i+1];
                            max[i+1] = max[i];
                            max[i] = cur;
                        }
                    }
                }
                cur = 0;
            } else
                cur += Integer.parseInt(line);
        }


        for(int i : max)
            ret += i;

        return ret;

    }

    private static int getMax(List<String> allLines) {
        int max = 0, cur = 0;

        for (String line : allLines) {
            if(line.equals("")) {
                if(cur > max)
                    max = cur;
                cur = 0;
            } else
                cur += Integer.parseInt(line);
        }

        return max;
    }

}

