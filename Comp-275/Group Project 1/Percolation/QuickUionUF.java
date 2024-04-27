public class QuickUionUF {
    private int[] parent;  // parent[i] = parent of i
    private int count;   // number of components
    public QuickUionUF(int n) {
        if (n < 0) throw new IllegalArgumentException();
        //create array parent(ie. id)
        parent = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        //initial value of count for tracking number of
        // connected set of components
        count=n;

    }

    public int count() {
        return count;
    }

    public int find(int p){

        return  this.parent[p];

    }

    public boolean connected(int p, int q) {

        return parent[p] == parent[q];

    }


    public int union(int p, int q){
        int pID =this.parent[p];
        int qID = this.parent[q];
        
        if (pID == qID) return 0; // p and q are already in 
		                          //the same component
        int numOfArrAccess=0;
        for (int i = 0; i < parent.length; i++)
            if (parent[i] == pID){
                parent[i] = qID;
                numOfArrAccess++;
            }
        count--;
        return  numOfArrAccess;
    }
}