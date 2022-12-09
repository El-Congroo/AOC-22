import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class SecondDay {

    public static void main (String args[]) {
        try {
            List<String> allLines = Files.readAllLines(Paths.get("/Users/lasse/Documents/Sammler/Code/AdventOfCode/src/input2.txt"));
            System.out.println("Your score would be: " + getScore(allLines));
            System.out.println("Your score in Game 2 would be: " + getScore2(allLines));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static int getScore2(List<String> allLines) {
        int scoreSum = 0;
        for(String line : allLines) {
            scoreSum += singleScore2(line);
            scoreSum += winDrawLose2(line);
        }

        return scoreSum;
    }

    private static int winDrawLose2(String line) {
        return (line.charAt(2)-88) * 3;
    }

    private static int singleScore2(String line) {
        int he = line.charAt(0)-65,
                should = line.charAt(2)-88;

        int[][] ret = {
                {3, 1, 2},
                {1, 2, 3},
                {2, 3, 1}
        };

        return ret[he][should];
    }


    private static int getScore(List<String> allLines) {
        int scoreSum = 0;
        for(String line : allLines) {
            scoreSum += singleScore(line);
            scoreSum += winDrawLose(line);
        }

        return scoreSum;
    }

    private static int winDrawLose(String line) {
        int he = line.charAt(0),
                me = line.charAt(2) - 23;

        switch (me - he) {
            case 0:
                return 3;       // DRAW
            case 1:
            case -2:
                return 6;       // WIN
            default:
                return 0;       // LOSE

        }
    }

    private static int singleScore(String line) {
        return line.charAt(2)-87;
    }

}
