import java.util.Arrays;
import java.util.Random;
public class Experiment {
    public static void main(String[] args) {
        StdRandom.setSeed(10);
        Comparable [] arr = new Comparable[10];
        for (int i=0;i<10;i++) {
            arr[i]=StdRandom.uniformDouble();

        }
        System.out.println(Arrays.toString(arr));
        //Selection_Sort.sort(arr);
        //Insertion.sort(arr);
        MergeBU.sort(arr);
        //Merge.sort(arr);
        System.out.println(Arrays.toString(arr));
    }

}

class StdRandom{
    private static Random random;
    private static long seed;
    static {
        seed=System.currentTimeMillis();
        random = new Random(seed);
    }

    public static void setSeed(long seed) {
//        StdRandom.seed = seed;
        random = new Random(seed);
    }

    public static double uniformDouble(){
        return random.nextDouble();
    }
}
