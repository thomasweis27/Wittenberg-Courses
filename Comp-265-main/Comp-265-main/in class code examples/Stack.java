//
// Name:
// File: Stack.java
// Date: Spring 2023
//
// Desc: Implements Stack example from Webber Ch 15
//

	public class Stack implements Worklist {
		private Node top = null;
	//	protected Node top = null;

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

}
			
	