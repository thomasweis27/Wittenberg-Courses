//
// File: GStack.java
//
// Desc: Generic Stack - See Webber page 287
//

	public class GStack<T> implements GWorklist<T> {
		private GNode<T> top = null;
		public void add(T data) {
			top = new GNode<T>(data, top);
		}
		public boolean hasMore() {
			return (top != null);
		}
		public T remove() {	
			GNode<T> n = top;
			top = n.getLink();
			return n. getData();
		}

	public static void main(String[] args) {

		GStack<String> s1 = new GStack<String> ();
		GStack<Integer> s2 = new GStack<Integer> ();
 		s1.add("hello");
		s1.add("world!");
		s2.add(17);
		s2.add(29);
		System.out.println(s1.remove());
		System.out.println(s1.remove());
		System.out.println(s2.remove());
		System.out.println(s2.remove());
	}
	
}		
		