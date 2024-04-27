public class programstructure{

public static void main(String[] args){
    //public - being able to access out of the program from another java file
    //static- when do you want to convert addresses to memory, 
        //another option can be dynamic but likely will never use
    //void - return type - what to send back when done
    //main - method/function name: name to call the function
    //parameters/arguments - preconduction function needed to get code to work
    String personname = "Brandon";
    boolean propername= true;

    if(personname.equals("Brandon")) //this is a one line if statement 
        propername = true; //this runs but anything below it will not be part of the if statement 
}
}
/*
 * Coupling
 * the degree of independance between software moduals
 * loose coupling is better - we don't want to make the same change to different areas of code
 * 
 * Coheasion
 * The degree that the elements inside a modual belong together
 * High coheasion is needed - one class that does it's job really well (and reused)
 */