//
// Name:
// File: StackDriver.java
// Date: Spring 2023
//
// Desc: Implements ConsCell example from Webber Text. 
//

public class StackDriver {

	public static void main(String[] args) {
		Worklist w;
		w = new Stack();
		w.add("the plow ");
		w.add("forgives ");
		w.add("The cut worm ");
		System.out.println();
		while (w.hasMore()){
			System.out.print(w.remove());
		}
		System.out.println();
	}
}		

			
	