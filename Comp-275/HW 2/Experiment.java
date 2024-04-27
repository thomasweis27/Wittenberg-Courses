import java.util.Arrays;
import java.util.Random;
public class Experiment {
    public static void main(String[] args) {
        int [] size={100,1000, 10000, 50000,100000,200000,300000,500000, 1000000 }; 
        Comparable [] arr ;
        for(int sz:size) {
            System.out.println("Time taken to sort "+ sz + " elements");
            for (int sortType = 1; sortType <= 6; sortType++) {//increase size type to 6 if you 
                arr = getRandomNumberArr(sz);                  //will be implementing the RADIX Sort
                invokeNextSortAlgo(sortType, arr);
            }
            System.out.println();
        }
    }

    public static void invokeNextSortAlgo(int sortType, Comparable []arr){
        switch (sortType){
            case 1://merge sort top-down approach
                Stopwatch.start();
                Merge.sort(arr);
                System.out.println("Merge TD sort time:" +Stopwatch.elapsedTime());
                break;


            case 2://merge sort bottom-up approach
                Stopwatch.start();
                MergeBU.sort(arr);
                System.out.println("Merge BU sort time:" + Stopwatch.elapsedTime());
                break;


            case 3: //quick sort
                Stopwatch.start();
                quick.sort(arr);
                System.out.println("Merge Quick sort time:" + Stopwatch.elapsedTime());
                break;


            case 4: //insertion sort
                Stopwatch.start();
                InsertionSort.sort(arr);
                System.out.println("Insertion sort time:" + Stopwatch.elapsedTime());
                break;


            case 5: //selection sort
                Stopwatch.start();
                selectionSort.sort(arr);
                System.out.println("Selection sort time:" + Stopwatch.elapsedTime());
				break;


			default: //Radix sort
			    //To-do: invoke Stopwatch start method
                Stopwatch.start();
                //To-do: invoke selection sort algorithm
                LSD.sort(arr, arr.length);
                //To-do:complete print statement by appending the stopwatch elapse time to it
                System.out.println("Radix sort time:" + Stopwatch.elapsedTime());
        }
    }

    public static Comparable[] getRandomNumberArr(int size){
        int n=size;
        StdRandom.setSeed(n);
        Comparable [] arr = new Comparable[n];
        for (int i=0;i<n;i++) {
            arr[i]=StdRandom.uniformDouble();
        }
        return arr;
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

   public static void shuffle(Comparable [] a){
        int n = a.length-1;
        for(int i=0; i<n;i++) {
            int r = random.nextInt(n) + 0;
            Comparable temp =a[i];
            a[i]=a[r];
            a[r]=temp;
        }
   }
}



