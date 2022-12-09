import java.util.List;

public class Day4 {

    private static int getScore2(List<String> list) {
        int ret = 0;

        for(String line : list) {
            int[] sections = parse(line);

            for(int i=0; i<4; i++)
                if (sections[i] >= sections[((i/2)*2 + 2) % 4] &&
                        sections[i] <= sections[((i/2)*2 + 3) % 4]) {
                    ret += 1;
                    break;
                }
        }
        return ret;
    }


    private static int getScore(List<String> list) {
        int ret = 0;

        for(String line : list) {

            int[] sections = parse(line);

            for(int i=0; i<4; i += 2)
                if(sections[i] >= sections[(i+2)%4] &&
                        sections[i+1] <= sections[(i+3)%4]) {
                    ret += 1;
                    break;
                }
        }

        return ret;
    }

    public static int[] parse(String s) {
        String[] splitted = s.split("[,-]");
        int[] sections = new int[4];
        for(int i=0; i<sections.length; i++)
            sections[i] = Integer.parseInt(splitted[i]);
        return sections;
    }
}
