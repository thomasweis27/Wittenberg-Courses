/**
 * Name: Thomas Weis
 * Semester/Year: SP23
 * Desc: ASIGNMENT 1 - NUMBER OF PRIMES TO DISPLAY
 * I Received Help From: none
 * 
 * I affirm that my work upholds the highest standards of honesty and academic integrity at
 * Wittenberg and that I have neither given nor received unauthorized assistance.
 */
import java.util.Scanner;

public class primes_asignment_1{
    public static void main (String[] args) {

          //gets an input
          Scanner keyboard = new Scanner(System.in);
          System.out.print("Please enter number of primes you'd like to see: ");
          int primeNum = 0;
          primeNum = keyboard.nextInt();
          keyboard.close();
          primeNum +=1;
          int isPrime = 0;
          for (int j = 2; j < primeNum+1; j+=1){
               isPrime = 0;
               for (int i = 2; i < j; i+=1){
               //System.out.print(j);
               //System.out.print(i);
               //System.out.print(j%i);
               //System.out.print("\n");
                    if(j % i == 0){
                         isPrime = 1;
                         //System.out.print("This runs so not prime");
                    }     
               
               }

          if(primeNum == 2){
               System.out.print(j);
          }
          else if(isPrime != 1){
               System.out.print(j);
               System.out.print(" ");
               
               //System.out.print("prime\n");
          }
          else if(isPrime ==1){
               primeNum +=1;
               //System.out.print(j);
               //System.out.print("not prime\n");
          }
          
          else{
               System.out.print("\nThis is not a prime number\n");
          }
          }
//lists
//String[] name = {One, To, Three};

     }
     
}
// needed for continuous user input: keyboard.nextLine();