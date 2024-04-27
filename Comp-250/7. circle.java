import java.lang.Math; 
import java.util.Scanner; 
class Main{

    //this gets the info from the user
    public static int getRadius(){
    
    Scanner keyboard = new Scanner(System.in);
    System.out.print("Enter in a radius: ");
    int radius = 0;
    radius = keyboard.nextInt();

    keyboard.close();
    return radius;
    }


    //calculates and returns area
    public static double calcArea(int radius){
        double area = 0;
        area = 4*Math.PI*Math.pow(radius, 2);
        return area;
        
    }






    public static void main(String[] arg) {
        int radius = getRadius();
        Double area = calcArea(radius);
        System.out.print("The radius of the given sphere is: " + area);
    }
}