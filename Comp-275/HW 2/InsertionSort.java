public class InsertionSort {
    public static void sort(Comparable [] a){
        for(int i=0;i<a.length;i++){
            for(int j=i;j>0 && less(a[j], a[j-1]);j--){
                swap(a,j,j-1);
            }
        }
    }
    public static boolean less(Comparable v, Comparable w){
        return v.compareTo(w)<0;
    }
    public static void swap(Comparable []a, int i, int j){
        Comparable temp = a[i];
        a[i]=a[j];
        a[j]=temp;
    }
}