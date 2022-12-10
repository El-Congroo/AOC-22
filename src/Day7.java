import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.regex.Pattern;

public class Day7 {

    public static int getScore(List<String> allLines) {
        int size = 0;
        Folder cur, root;
        LinkedList<Folder> path = new LinkedList<>();
        root = new Folder("/");
        cur = root;

        // creating basic Folder structure
        for(String line : allLines) {

            String[] s = line.split(" ");
            if(s[0].equals("$") && s[1].equals("cd")) {
                if(s[2].equals("..")) {
                    cur = path.removeLast();
                } else if(s[2].equals("/")) {
                    cur = root;
                    path = new LinkedList<>();
                } else {
                    Folder tmp = new Folder(s[2]);
                    cur.addFolder(tmp);
                    path.add(cur);
                    cur = tmp;
                }
            } else if(Pattern.compile("-?\\d+(\\.\\d+)?").matcher(s[0]).matches()) {
                cur.addSize(Integer.parseInt(s[0]));
            }
        }

        root.setCorrectSize();

        final int need = 30_000_000;
        final int space = 70_000_000;
        int liberate = need - (space - root.getSize());

        return root.libMin(liberate);
        // return root.sumSmaller100k();
    }



}

class Folder {
    private int size;
    private List<Folder> kids;
    private String name;

    Folder(String s) {
        name = s;
        size = 0;
    }

    public String getName() {
        return name;
    }

     public void addSize(int i) {
        size += i;
    }

    public int getSize() {
        return size;
    }

    public void addFolder(Folder f) {
        if(kids == null)
            kids = new ArrayList<>();
        kids.add(f);
    }

    public List<Folder> getKids() {
        if(kids == null)
            return new ArrayList<>();
        return kids;
    }

    public int setCorrectSize() {
        for(Folder kid : getKids())
            addSize(kid.setCorrectSize());
        return getSize();
    }

    public int sumSmaller100k() {
        int sum = 0;
        for(Folder kid : getKids())
            sum += kid.sumSmaller100k();

        if(getSize() <= 100_000)
            sum += getSize();


        return sum;
    }

    public int libMin(int liberate){
        int min = getSize();
        for(Folder kid : getKids())
            if(kid.getSize() >= liberate)
                min = Math.min(kid.libMin(liberate), min);
        return min;
    }
}