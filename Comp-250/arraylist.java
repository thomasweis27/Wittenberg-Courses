import java.util.ArrayList;

class arraylist{
    public static char computerSays(){
        // return r, g, or b
        char computerSays = ' ';
        return computerSays;
    }

    public static ArrayList<Character> playerSays(){
        ArrayList<Character> playerSays = new ArrayList<Character>();
        playerSays = null;
    }

    public static void main(String[] args){
        //char[] name = new char[size]; <-- how to do a basic array
        ArrayList<Character> computersequence = new ArrayList<Character>();

        //Method one: computer says a character
            //char computerSays = computerSays();
            //computerSequence.add(computerSays());

        //method two: does the same as above but usues less memory
        computerSequence.add(computerSays());


        playerSequence = playerSays();
        
    }
} 