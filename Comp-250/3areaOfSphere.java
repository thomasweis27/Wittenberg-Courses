import java.util.Scanner;
import java.lang.Math.PI;

class main {
    public static void main(String[] arge){
        Scanner userinput = new Scanner(System.in);
        System.out.print("Enter the raduis: ");
        //ask the user for an input
        int radius = 0;
        radius = userinput.nextInt();

        //do the math
        double area1 = 4* Math.PI *radius * radius;

        //round and print to 2 values
        System.out.printf("The area is: %.2f\n", area1);
    }
}