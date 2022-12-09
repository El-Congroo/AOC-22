import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class FourthDay{

    public static void main(String[] args) {
        try {
            List<String> allLines = Files.readAllLines(Paths.get("/Users/lasse/Documents/Sammler/Code/AdventOfCode/src/input4.txt"));
            System.out.println("Your score would be: " + getScore2(allLines));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

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
