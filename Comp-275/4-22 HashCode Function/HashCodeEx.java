public class HashCodeEx {
    //private int x;
    //private int y;

    private static String m; //array size
    public static void main(String[] args){
        String name = "Mark";
        m = 5;
        int hashCode=0;
        for (int key=0; key<m.length(); key++){
            key = name.carAt(key);
            hashCode =+ System.out.println(hashMod(key, m));
        }
        System.out.println("The hashcode for 'Mark' is ", hashCode);
    }

    //his code didn't ompit m into this function but it gave me errors when I didn't do this.
    public static int hashMod(int key, int m){
        int hashCode;
        hashCode = key%m;
        return hashCode;
    }

}