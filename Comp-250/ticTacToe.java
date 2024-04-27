import java.util.Scanner;

class ticTacToe{
    public static void main(String[] args){

        //create a board
        char[][] board = new char[3][3];

        // //get the user's names
        // Scanner keyboard = new Scanner(System.in);
        // System.out.print("Player 1 Name (x): ");
        // String player1 = "";
        // player1 = keyboard.nextInt();
        // System.out.print("Player 2 Name (o): ");
        // String player2 = " ";
        // player2 = keyboard.nextInt();
        // keyboard.close();

        char playerOne = 'x';
        char playerTwo = 'o';

        int turn = 0;
        char currentplayer = '-';

        while(true){
            for(int x= 0; x <3; x++){
                for(int y = 0; y <3; y++){
                    board[x][y] = '-';
                }
            }
            if(turn %2 == 0){
                currentplayer = playerOne;
            }
            else{
                currentplayer = playerTwo;                
            }
        }
    }
}



