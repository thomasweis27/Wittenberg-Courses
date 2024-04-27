public class test{
    public static void main(String[] args){
        //  Declare and Initialize 10 elements of Integer Array
        int[] myValues = new int[] { 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 }; 
        int[] newValues = new int[10];
        //1.  Iterate through every element of the Integer Array
        for(int i = 0; i < 10; i++){
        //2.  Increment each element by 1.
        int x = (myValues[i]+1);
        System.out.print(x + " ");
        newValues[i] = x; 
    }
    
    
    //3.  Store the new value back into the Array
    myValues = newValues;

    }
}