//Thomas Weis
//I affirm that my work upholds the highset standards of honesty and academic integrity 
//      at wittenberg and that I have neither given or recieved unauthorised assistance.

import java.util.*;
public class Driver02 {
	static Scanner scanner = new Scanner(System.in);

	//slide three from 3/15
	public static class ConsCell {
		private int head;
		private ConsCell tail;
		
		public ConsCell(int h, ConsCell t) {
			head = h;
			tail = t;
		}
		public int getHead() {
			return head;
		}
		public ConsCell getTail() {
			return tail;
		}
		public void setTail(ConsCell t) {
			tail = t;
		}
	}
	
	//slide four from 3/15
	public static class IntList {
		private ConsCell start;
		
		public IntList(ConsCell s) {
			start = s;
		}
		public IntList cons(int h) {
			return new IntList(new ConsCell(h,start));
		}

		public int length() {
			int len = 0;
			ConsCell cell = start;
			while (cell != null) {
				len++;
				cell = cell.getTail();
			}
			return len;	
		}
		
		public void print(){
			System.out.print("[");
			ConsCell a = start;
			while (a != null) {
				System.out.print(a.getHead());
				a = a.getTail();
				if (a != null) System.out.print(",");
			}
			System.out.println("]");
		}
//================================================================================================================
// code to see if the item exists in the following
	public void contains(int x){
			//bool TF = true;
            ConsCell a = start;
			while (a != null) {
                if (a.getHead() == x){
                    //return TF;
					System.out.print(x + " is in IntList (true)\n");
					break;
                } else{
				a = a.getTail();
				}
			}
			if (a == null){
				//TF = false;
				//return TF;
				System.out.println(x + " was not found (false)");
        	}
		}
	}
//___________________________________________________________________________________________________

	public static void main(String[] args) {
		int k;
		IntList a = new IntList(null);
		System.out.print("\nEnter an integer (0 to quit)\n?: ");
		k = scanner.nextInt();
		while (k != 0){
                a = a.cons(k);
                a.print();
			System.out.print("?: ");
			k = scanner.nextInt();
		}
		int x = a.length();
		a.print();
		System.out.print("The length is " + x);


//checks to see if the item is listed from above
        k--;
        System.out.print("\nEnter a search integer (0 to quit)\n?: ");
        k = scanner.nextInt();
        while (k != 0){
            a.contains(k);
        	System.out.print("?: ");
        	k = scanner.nextInt();
    	}
	System.out.print("End of program.");
	}
}