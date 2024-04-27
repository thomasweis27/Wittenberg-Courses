
import java.util.Arrays;

public class Percolation 
{

  int top; // quickunion id of top node/site/box
  int[] bottom; // array of quickunion ids for last row of boxes

  //COMMENT OUT THE ONE NOT WANTED - QuickUionUF OR WeightedQuickUnionUF NEED TO CHANGE THIS ONCE BELOW TO SWITCH BETWEEN UNION TYPES
  //QuickUionUF qunion; 
  WeightedQuickUnionUF qunion;

  boolean[][] grid; // 2d grid of booleans
  int size; // the size of one of the sides of the grid
  int open_sites;

  public Percolation(int n) {
      // Throw exception if n<0
      if (n < 0) { throw new java.lang.IndexOutOfBoundsException("n needs to be greater than 0"); }
  
      // set the union ids of the top and bottom sites
      this.top = 0;
      this.bottom = new int[n];
  
      // calculate and fill the qunion ids for the last row of boxes
      for (int x = 0; x < n; x++) 
      {
          this.bottom[x] = (n * (n - 1) + 1) + x;
      }
  
      // initialize boolean array
      this.grid = new boolean[n][n];
  
      // INIT THE CORRECT QUICK UNION. COMMENT OUT THE METHOD NOT WANTED TO RUN FOR THE RIGHT QUICK UNION IMPLEMENTATION.
      //this.qunion = new QuickUionUF(n * n + 2);
      this.qunion = new WeightedQuickUnionUF(n * n + 2);
      this.size = n;
  
      this.open_sites = 0;
  }

  public void open(int row, int col) 
  {
      // set the given box as "open" and connect it to any other adjacent open boxes
      // in the quick union object
  
      // error if the coordinates don't make sense
      if (row < 0 || row >= this.size) { throw new java.lang.IndexOutOfBoundsException("row out of range"); }
      if (col < 0 || col >= this.size) { throw new java.lang.IndexOutOfBoundsException("column out of range"); }
  
      // return if site is already open
      if (this.grid[row][col] == true) { return; }
  
      // check if surrounding sites are open and qunion connect them if they are
  
      // unionfind ids for each site/box
      int currentbox_id = row * this.size + col + 1;
      int leftbox_id = currentbox_id - 1;
      int rightbox_id = currentbox_id + 1;
      int topbox_id = currentbox_id - this.size;
      int bottombox_id = currentbox_id + this.size;
  
      // if top row, connect immediately to the relevant node
      if (row == 0) { this.qunion.union(currentbox_id, 0); }
  
      // check site directly to the left
      if (col - 1 >= 0 && this.isOpen(row, col - 1)) { this.qunion.union(currentbox_id, leftbox_id); }
  
      // check site directly to the right
      if (col + 1 < this.size && this.isOpen(row, col + 1)) { this.qunion.union(currentbox_id, rightbox_id); }
  
      // check site directly above
      if (row - 1 >= 0 && this.isOpen(row - 1, col)) { this.qunion.union(currentbox_id, topbox_id); }
  
      // check site directly below
      if (row + 1 < this.size && this.isOpen(row + 1, col)) { this.qunion.union(currentbox_id, bottombox_id); }
  
      // set the box to "open" in the grid and increment open site counter
      this.grid[row][col] = true;
      this.open_sites += 1;
  
  }

  public boolean isOpen(int row, int col) 
  {
      // returns whether or not the given box is open
  
      // error if the coordinates don't make sense
      if (row < 0 || row >= this.size) { throw new java.lang.IndexOutOfBoundsException("row out of range"); }
      if (col < 0 || col >= this.size) { throw new java.lang.IndexOutOfBoundsException("column out of range"); }
  
      return this.grid[row][col];
    }

  public int numberOfOpenSites() 
  {
      // returns the number of open sites in the grid
      return this.open_sites;
    }

  public boolean isFull(int row, int col) 
  {
    // error if the coordinates don't make sense
      if (row < 0 || row >= this.size) { throw new java.lang.IndexOutOfBoundsException("row out of range"); }
      if (col < 0 || col >= this.size) { throw new java.lang.IndexOutOfBoundsException("column out of range"); }
  
      // returns true when the given box is connected to the top of the grid
      return this.qunion.connected(this.top, row * this.size + col + 1);
  }

  public boolean percolates() 
  {
      // loop through the qunion id of each box in the bottom row
      for (int x = 0; x < this.size; x++) 
      {
          // if one of the boxes is connected, return true
          if (this.qunion.connected(this.top, this.bottom[x])) { return true; }
      }
  
      // none of the boxes are connected to the top if we make it here :(
      return false;
  }

  public void printArray() 
  {
      // prints the grid to the console
      for (int x = 0; x < this.size; x++) 
      { 
          Arrays.toString(this.grid[x]); 
      }
  }
}
