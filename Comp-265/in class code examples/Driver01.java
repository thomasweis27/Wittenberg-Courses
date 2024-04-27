//
// Name:
// File: Driver01.java
// Date: Spring 2023
//
// Desc: Implements ConsCell example from Webber Text. 
//

import java.util.*;

public class Driver01 {
	
	static Scanner scanner = new Scanner(System.in);

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

	public static class IntList {
		private ConsCell start;
		
		public IntList(ConsCell s) {
			start = s;
		}
		public IntList cons(int h) {
			return new IntList(new ConsCell(h,start));
		}

                public int decons() {
                        if (start != null) {
                           int k = start.getHead(); 
                           start = start.getTail();
                           return k;
	                }
                        else return 0;
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
		
		public boolean contains(int k){
			ConsCell a = start;
			while ((a!= null) && (k != a.getHead())) {
				a = a.getTail();
			}
			if (a == null)
				return false;
			else 
				return (k == a.getHead());
		}
	}
	
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
		System.out.print("Length = " + x);
		System.out.println("\nEnd of Pgm");
	/*		
		IntList a = new IntList(null);
		IntList b = a.cons(2);
		IntList c = b.cons(1);
		int x = a.length() + b.length() + c.length();
		a.print();
		b.print();
		c.print();
		System.out.println(x);
	*/
		
	}

}
