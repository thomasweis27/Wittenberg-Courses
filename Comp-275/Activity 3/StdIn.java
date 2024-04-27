
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class StdIn {
    private static FileInputStream f;
    private static Scanner reader= new Scanner(new InputStreamReader(System.in));
    private static boolean initialread;
   public StdIn(){

   }
    public StdIn(String [] args) throws FileNotFoundException {
        String filename = args[0];
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

       return !reader.hasNextLine();

    }

}
