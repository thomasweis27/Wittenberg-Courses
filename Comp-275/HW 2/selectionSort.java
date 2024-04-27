import java.util.Arrays;

public class selectionSort {
    //main method tests a given array and prints the origional and sorted array
    

    //almost same as class slides
    //slides missing {} for if, & for statements
    public static void sort(Comparable[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (less(a[j], a[min])) {
                    min = j;
                }
            }
            exch(a, i, min);
        }
    }
    
    //same as on class slides
    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    //almost the same as the class slides
    //changed Object to Comparable
    private static void exch(Comparable[] a, int i, int j) {
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }
}
