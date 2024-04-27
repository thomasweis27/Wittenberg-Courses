import java.io.*;
import java.util.Scanner;

public class finalproject {

    public static void listNotes(){
        string notesInScale = "A A# B C C# D D# E F F# G G# A A# B C C# D D# E F F# G G#"; //make this a list, good for skipping around steps and skips
        int counter = 0;
        while (notesInScale.charAt(counter) != 'B'){counter+=1;}
        counter+=1;
        while (notesInScale.charAt(counter) != 'B'){
            System.out.print(notesInScale.charAt(counter));    
            counter+=1;
        }
        
        System.out.print("This runs.");

    }



    public static void main(String[] args){
        
        Scanner keyboard = new Scanner(System.in);
        System.out.print("\nWelcome!\nPlease enter a key followed by M or m for major or minor: \n(Please notate sharps as '#' and flats as 'b') ");
        String startingKey = "";
        startingKey = keyboard.next();

        if (startingKey.charAt(startingKey.length()-1) == 'm'){
            System.out.print("You chose minor");
            listNotes();
            //say the notes in the key for minor
            System.out.print("The relative key for " + startingKey + " is INSERT METHOD HERE"); //change this to show the relative key
        }
        else if (startingKey.charAt(startingKey.length()-1) == 'M'){
            System.out.print("You chose Major\n");
            //say the notes in the key for major
            System.out.print("The relative key for " + startingKey + " is INSERT METHOD HERE"); //change this to show the relative key
        }
        else {
            System.out.print("\nDon't forget to notate 'M' or 'm' for major or minor at the end.\nThese little things are quite important in music theory.\n");
        }

    keyboard.close();
    }
}