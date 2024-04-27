import java.util.ArrayList;

public class ThreeSum {

    // Do not instantiate.
    private ThreeSum() {

    }

  
    public static int count(int[] a) {
        int n = a.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                for (int k = j+1; k < n; k++) {
                    if (a[i] + a[j] + a[k] == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    /**
     * Reads in a sequence of integers from a file, specified as a command-line argument;
     * counts the number of triples sum to exactly zero; prints out the time to perform
     * the computation.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) throws Exception {
        //read array from file
        ArrayList<Integer> arr = new ArrayList<Integer>();
        if (args.length==1)
            new StdIn(args);

        while (!StdIn.isEmpty()){
            arr.add(StdIn.readInt());
        }
        int []a = arr.stream().mapToInt(i->i).toArray();

        Stopwatch timer = new Stopwatch();
        timer.start();
        int count = count(a);
        timer.elapsedTime();
        System.out.println("elapsed time = " + timer.elapsedTime());
        System.out.println(count);
    }
}
