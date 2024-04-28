import java.util.Objects;
public class HashCodeGen {
    public static long naiveXYhashMod(String key, int m){
        long hashCode = 0;
        int x = key.charAt(0);
        int y = key.charAt(1);
        
        hashCode=(x+y)%m;
        return hashCode;
    }

    public static long efficientXYhashMod(String key, int m, int k){
        long hashCode = 0;
        int x = key.charAt(0);
        int y = key.charAt(1);
        
        hashCode=(k*x+y)%m;
        return hashCode;
    }

    public static long XORhash(String key, int bitShift){
        long hashCode = 0;
        int x = key.charAt(0);
        int y = key.charAt(1);
        int bits = (x*y);
        hashCode=(bits^(bits>>>bitShift));
        return hashCode;
    }

    public static long ObjectHashCode(String key){
        //long hashCode = 0;
        int x = key.charAt(0);
        int y = key.charAt(1);
        return Objects.hash(x*y);
    }
}
