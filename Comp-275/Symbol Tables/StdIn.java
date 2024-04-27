
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.NoSuchElementException;
public class StdIn {
    private static FileInputStream f;
    private static Scanner reader= new Scanner(new InputStreamReader(System.in));
    private static boolean initialread;
   public StdIn(){

   }
    public StdIn(String [] args) throws FileNotFoundException {
        String filename = args[1];
        f = new FileInputStream(filename);
        reader = new Scanner(new InputStreamReader(f));
    }
    public static int readInt(){
       if(!initialread){
           initialread=true;
           return Integer.parseInt(reader.nextLine());
       }

        return Integer.parseInt(reader.next());
    }

    public static boolean isEmpty(){

       //return !reader.hasNextLine();
        //System.out.println(!reader.hasNext());
        return !reader.hasNext();

    }
    public static String readString() {
        try {
            return reader.next();

        }
        catch (Exception e) {
            throw new NoSuchElementException("attempts to read a 'String' value from standard input, "
                    + "but no more tokens are available");
        }
    }
}
