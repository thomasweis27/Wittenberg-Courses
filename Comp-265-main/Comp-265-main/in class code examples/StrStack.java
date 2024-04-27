//
// Name:
// File: StrStack.java
// Date: Spring 2023
//
// Desc: Implements StrStack example from Webber Text Ch 15. 
//

	public class StrStack implements Worklist {
		private Node top = null;

	public void add	(String data) {
		top = new Node(data, top);
	}

	public boolean hasMore() {
		return (top != null);
	}

	public String remove () {
		Node n = top;
		top = n.getLink();
		return n.getData();
	}

	public static void main(String[] args) {
	Worklist w;
	w = new Stack();
	w.add("the plow ");
	w.add("forgives ");
	w.add("The cut worm ");
	System.out.print(w.remove());
	System.out.print(w.remove());
	System.out.println(w.remove());
	}

}		

			
	