import java.io.FileNotFoundException;

public class FrequencyCounter  {
    public static void main(String[] args) throws FileNotFoundException{
        int minlength = Integer.parseInt(args[0]);
        ST<String, Integer> st = new ST<>();
        new StdIn(args); //add Exception;
    while (!StdIn.isEmpty()){
        String word = StdIn.readString();
        if (word.length() < minlength) {continue;}
        if (!st.contains(word)) {st.put(word, 1);}
        else {st.put(word, st.get(word) + 1);}
}
    String champ = "";
    st.put(champ, 0);
    for (String word: st.keys()) {
    if (st.get(word) > st.get(champ)){
        champ = word;
        }
    }
    System.out.println(champ + " " + st.get(champ));
    }
}