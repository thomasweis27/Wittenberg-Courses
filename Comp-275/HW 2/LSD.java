public class LSD {
    public static void sort(Comparable[] a, int W){
        int N = a.length;
        int R = 256;
        Object[] aux = new Object[N];
        
        for (int d = W - 1; d >= 0; d--) { // Sort by key-indexed counting on dth char.
            int[] count = new int[R + 1]; // Compute frequency counts.
            
            for (int i = 0; i < N; i++) {
                int c = getDigit((Double)a[i], d, W);
                count[c + 1]++;
            }
            for (int r = 0; r < R; r++) { // Transform counts to indices.
                count[r + 1] += count[r];
            }
            for (int i = 0; i < N; i++) { // Distribute.
                int c = getDigit((Double)a[i], d, W);
                aux[count[c]++] = a[i];
            }
            for (int i = 0; i < N; i++) { // Copy back.
                a[i] = (Comparable) aux[i];
            }
        }
    }

    // Get the digit at the specified position - origional program worked for strings so needed to be fixed for ints/doubles
    private static int getDigit(Double value, int position, int W) {
        double divisor = Math.pow(10, W - position - 1);
        return (int) ((value / divisor) % 10);
    }
}
