import java.util.List;

public class Day02 {

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

}

