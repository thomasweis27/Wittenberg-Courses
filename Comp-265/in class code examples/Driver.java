//
// Name;
// File: Driver.java
// Date: March 15, 2023
//
// Desc: Java code example presented in Comp 265 class 
//

public class Driver{
	public static class ConsCell{
		private int head;
		private ConsCell tail;
		public ConsCell(int h, ConsCell t){
			head = h;
			tail = t;
		}
		public int getHead(){
			return head;
		}
		public ConsCell getTail(){
			return tail;
		}
		public void setTail(ConsCell t){
			tail = t;
		}
	}
	public static class IntList{
		private ConsCell start;

		public IntList(ConsCell s){
			start = s;
		}
		public IntList cons(int h){
			return new IntList (new ConsCell (h,start));
		}
		public int length(){
			int len = 0;
			ConsCell cell = start;
			while (cell != null){
				len++;
				cell = cell.getTail();
			}
			return len;
		}
		public void print() {
			System.out.print("[");
			ConsCell a = start;
			while (a != null) {
				System.out.print(a.getHead());
				a = a.getTail();
				if (a != null) System.out.printf(",");
			}
			System.out.println("]");
		}
		
	}

	public static void main(String[] args){
		IntList a = new IntList(null);
		IntList b = a.cons(2);
		IntList c = b.cons(1);
		int x = a.length()+b.length()+c.length();
		a.print();
		b.print();
		c.print();
		System.out.println(x);
	}
}

