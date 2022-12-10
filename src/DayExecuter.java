import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.regex.Pattern;

public class DayExecuter extends Day7 {

    public static void main (String[] args) {

        try {
            List<String> allLines = Files.readAllLines(Paths.get("data/input7.txt"));
            System.out.println("Your score would be: " + getScore(allLines));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
