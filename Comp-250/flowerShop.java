/*
Name: Thomas Weis
Semester/Year: SP 2023
Desc: Flower shop: make a program that checks invantoy and give a recept
I Received Help From: XX
I affirm that my work upholds the highest standards of honesty and academic integrity at
Wittenberg and that I have neither given nor received unauthorized assistance.
Thomas Weis
*/

//Note: this works if more flower and more values are all added to txt file. 


import java.io.*;
import java.util.Scanner;

public class flowerShop {
    public static void main(String[] args) throws Exception {
        File outFile = new File("C:\\Users\\thoma\\Desktop\\Comp 250\\asignments\\flower shop\\Recipt.txt");
        FileWriter output = new FileWriter(outFile);

        FileReader fr = new FileReader("C:\\Users\\thoma\\Desktop\\Comp 250\\asignments\\flower shop\\Flowers.txt");
        int i;
        String fullText = "";
        while((i=fr.read())!=-1){
            //System.out.print((char) i);
            fullText = fullText + (char) i;
        }
 
        


        System.out.println("Thank you for visiting the Flower Shop!");
        System.out.println("A list of our current blooming flowers are:  ");
        System.out.print(fullText);



        boolean keepBuying = true;
        while(keepBuying == true){



        //get the inputs from the user to see what they want from the shop
        Scanner keyboard = new Scanner(System.in);
        System.out.print("\n\nPlease enter flower type you want to buy: \n(Or 'End' to end your shopping experiance.)");
        String flowerToBuy = "";
        flowerToBuy = keyboard.next();

        //System.out.print(flowerToBuy);
        if(flowerToBuy.equals("End")) {
            System.out.print("\n\n\n\nYou want to end the program.\nGoodbye");
            
            break;}
        
        System.out.print("Please enter # of flowers you want: ");
        int flowerNumber = 0;
        flowerNumber = keyboard.nextInt();
        



//check to make sure that we have that flower in stock
        int counter = 0;
        while (flowerToBuy.charAt(0) != fullText.charAt(counter) && counter < fullText.length()-1){ 
            counter += 1;
        }
        if ((counter+1) == fullText.length()){
            System.out.print("\nSorry, but I don't think that's in stock right now...\nMaybe try getting something else?");
        }
        else if (fullText.charAt(counter+1) == flowerToBuy.charAt(1) && fullText.charAt(counter+2) == flowerToBuy.charAt(2)){
            System.out.print("\nWe have that!\n");
            


//figure out the prices of the flowers
            while (fullText.charAt(counter) != ' '){
                counter += 1;
                //System.out.print(fullText.charAt(counter));
            }
            counter += 1;
            String indPrice = "";
            while (fullText.charAt(counter) != ' '){
                indPrice = indPrice +fullText.charAt(counter);
                counter += 1;
            }
            System.out.print("\nThe indevidual price is $" + indPrice);
            counter+=1;

            String bqPrice = "";
            while (fullText.charAt(counter) != '\n'&& counter != fullText.length()-1){
                bqPrice = bqPrice +fullText.charAt(counter);
                counter += 1;
            }
            System.out.print("\nThe bouqet price is $" + bqPrice);

            //make the string a double
            Double bqDouble = Double.valueOf(bqPrice); // returns Double object
            //System.out.println(bqDouble);
            Double indDouble = Double.valueOf(indPrice); // returns Double object
            //System.out.println(indDouble);

            System.out.println("You would like "+ flowerNumber + " flowers for a price of $" +indDouble + " for a total of $"+ indDouble*flowerNumber);
            System.out.println("\nYour options are: \n    1. Bouquet for $"+ bqPrice + " \n    2. Indevidual for $" +indDouble*flowerNumber + "\nWhich would you perfer (1 or 2)?");
            
            int oneOrTwo = 0;
            oneOrTwo = keyboard.nextInt();
            System.out.println("\nSounds good! Would you like another flower type too?");
            System.out.print("\n\n");

            if(oneOrTwo == 2){
                output.write("[" + flowerToBuy + "] [Individual] " + "[#: " + flowerNumber + "] " + "[$" + indDouble*flowerNumber + "] \n");
            }
            else if(oneOrTwo == 1){
                output.write("[" + flowerToBuy + "] [Bouquet] " + "[#: " + flowerNumber + "] " + "[$" + indDouble*flowerNumber + "] \n");
            }
        }
        else{
            System.out.print("\nSorry, but I don't think that's in stock right now...\nMaybe try getting something else?");
    }   }
    output.close();
}   }