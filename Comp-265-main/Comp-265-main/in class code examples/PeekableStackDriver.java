//
// File:  PeekableStackDriver.java
//
// Desc: Driver file for PeekableStack extension
// 	

public class PeekableStackDriver {

	public static void main(String[] args) {
		PeekableStack s = new PeekableStack();
		s.add("drive");
		s.add("cart");
		s.remove();
		System.out.println(s.peek());
	}
}
