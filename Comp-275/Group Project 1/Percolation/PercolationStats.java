import java.lang.Math;
import java.util.ArrayList;

public class PercolationStats {

    // Constants:
    private static double CONFIDENCE = 1.96;

    // Class variables:
    private double[] fractions;
    int numOpenSites;

    public PercolationStats(int n, int t) {
        
        this.fractions = new double[t];

        //t = number of simulations
        //n = number of grid n*n
        for (int a = 0; a < t; a++) {
            Percolation percolation = new Percolation(n);
            numOpenSites = 0;
          
            // runs until the system percolates
            while (!percolation.percolates()) 
            {
                int i = StdRandom.uniform(0, n);
                int j = StdRandom.uniform(0, n);

                if (!percolation.isOpen(i, j)) 
                {
                    percolation.open(i, j);
                    numOpenSites++;
                }
                
            }

            // fraction of open sites to total sites and adds to array.
            double openSitesFrac = (double) numOpenSites / (double) (n*n);
            this.fractions[a] = openSitesFrac;
        }
    }

    public double mean() {
        Double mean = StdStats.mean(this.fractions);
        return mean;
    }

    public double stddev() {
        Double StdDev = StdStats.stddev(this.fractions);
        return StdDev;
    }

    public double confidenceLow() {
        Double confidenceLow = (mean() - (CONFIDENCE * StdStats.stddev(fractions)) / Math.sqrt(numOpenSites));
        return confidenceLow;
    }

    public double confidenceHigh() {
        Double confidenceHigh = (mean() + (CONFIDENCE * StdStats.stddev(fractions)) / Math.sqrt(numOpenSites));
        return confidenceHigh;
    }

    public static void main(String[] args) {
        // define the values n and t by passing it as an argument to your program main()
        // method or hardcoding it
        int n = 100;
        int t = 700;
        Stopwatch.start();
        PercolationStats percolationStats = new PercolationStats(n, t);
        
        //display the requested for information:
        System.out.println("Elapsed Time: "+Stopwatch.elapsedTime());
        System.out.println("Mean Value: " + percolationStats.mean());
        System.out.println("Standard Dev: " + percolationStats.stddev());
        System.out.println("Confidence Low: " + percolationStats.confidenceLow());
        System.out.println("Confidence High: " + percolationStats.confidenceHigh());
        
    }
}
