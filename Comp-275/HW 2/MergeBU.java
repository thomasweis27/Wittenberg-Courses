public class MergeBU{

    private void merge(){}
    public static void merge(Comparable [] a, Comparable [] aux, int lo, int mid, int hi){
        for (int k = lo; k <= hi; k++){
            aux[k] = a[k];
        }

        int i =lo; int j = mid+1;
        for (int k = lo; k <= hi; k++) {
            if (i > mid) {a[k] = aux[j++];}
            else if (j > hi) {a[k] = aux[i++];}
            else if (less(aux[j], aux[i])) {a[k]=aux[j++];}
            else {a[k] = aux[i++];}
        }
    }

    public static boolean less(Comparable v, Comparable w){
        return v.compareTo(w)<0;
    }
    

    public static void sort(Comparable[] a, Comparable[] aux, int lo, int hi) {
        if (hi <= lo) return;
        int mid = lo + (hi - lo) / 2;
        sort(a, aux, lo, mid);
        sort(a, aux, mid+1, hi);
        merge(a, aux, lo, mid, hi);
    }
        
    // public static void sort(Comparable[] a) {
    //    Comparable[] aux = new Comparable[a.length];
    //    sort(a, aux, 0, a.length - 1);
    // }


    public static void sort(Comparable[] a) {
        int n = a.length;
        Comparable[] aux = new Comparable[n];
        for (int sz = 1; sz < n; sz = sz+sz)
        for (int lo = 0; lo < n-sz; lo += sz+sz)
        merge(a, aux, lo, lo+sz-1, Math.min(lo+sz+sz-1, n-1));
        }
        
}