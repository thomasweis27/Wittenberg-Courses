import java.util.Arrays;
import java.util.Collections;

public class Experiment {
    public static void main(String[] args) {
        Comparable[] arr = new Comparable[10];
        for (int i = 0; i < 10; i++) {
            arr[i] = Math.random();
        }
        System.out.println("Origional Array: "+ Arrays.toString(arr));
        Quick.sort(arr);
        System.out.println("Sorted Array: "+ Arrays.toString(arr));
    }
}
/////////////////////////////////////////////////////////////////////////
class Quick {
    public static void sort(Comparable[] a) {
        shuffle(a); // Shuffling the array
        sort(a, 0, a.length - 1);
    }

    private static void sort(Comparable[] a, int lo, int hi) {
        if (hi <= lo) return;
        int j = partition(a, lo, hi);
        sort(a, lo, j - 1);
        sort(a, j+1, hi);
    }

    private static int partition(Comparable[] a, int lo, int hi) {
        Comparable p = a[lo];
        int i = lo, j = hi + 1;
        while (true) {
            while (less(a[++i], p)) {
                if (i == hi) break;
            }
            while (less(p, a[--j])) {
                if (j == lo) break;
            }
            if (i >= j) break;
            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    private static void exch(Comparable[] a, int i, int j) {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

    // Shuffling method using Collections.shuffle()
    private static void shuffle(Comparable[] a) {
        Collections.shuffle(Arrays.asList(a));
    }
}
