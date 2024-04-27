import java.io.IOException;

public class QuickFindClient {

    public static void main(String[] args) throws IOException {
        int N=0;
        if (args.length==1)
            new StdIn(args);
        N= StdIn.readInt();
        QuickFindAPI uf = new QuickFindAPI(N);
        Double totalTime=0.0;
        while (!StdIn.isEmpty()){
            int p = StdIn.readInt();
            int q = StdIn.readInt();

            if (!uf.connected(p,q)){
                //time for union operation of all the items
                //time for find operation for any given item
                Stopwatch.start();
                int n= uf.union(q,p);
//                int n= uf.union(q,p);
                totalTime+=Stopwatch.elapsedTime();
                System.out.println("Union("+ p + "," + q + ")\t takes \t"+ n + "\t array access");

            }
        }
        System.out.println("We have " + uf.count() + " sets of connected components");
        System.out.println("Total time taken in formation of the "+ uf.count() +
                " sets of connected components is " + (int) (totalTime*1000+0.5)/1000.0);
   }
}