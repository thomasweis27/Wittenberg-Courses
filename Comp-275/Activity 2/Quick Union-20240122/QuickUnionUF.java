
public class QuickUnionUF {
    private int[] parent;  // parent[i] = parent of i
    private int count;     // number of components
    private static int numArrayAccess;
    public QuickUnionUF(int n) {
        parent = new int[n];
        count = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int count() {

        return count;

    }

    public int[] find(int p) {
        numArrayAccess=1;
        int retval[]={0,0};
        while (p != parent[p]) {
            p = parent[p];
            numArrayAccess++;

        }
        retval[0]=p;
        retval[1]=numArrayAccess;
        return retval;
    }
    public boolean connected(int p, int q) {
            int [] p1=find(p);
            int [] q1=find(q);
        return p1[0]== q1[0];
    }

    public int union(int p, int q) {
        int totalNumArrayAccess=0;
        int [] rootP = find(p);
        totalNumArrayAccess=rootP[1];
        int [] rootQ = find(q);
        totalNumArrayAccess+=rootQ[1]-1;
        parent[p] = q;
        count--;
        return totalNumArrayAccess;
    }
}
