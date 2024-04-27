//
// File: GStackDriver.java
//
// Desc: Generic Stack - See Webber page 287
//

public class GStackDriver {

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
		