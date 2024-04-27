//
// File: PeekableStack.java
//
// Desc: Extends Stack class - see Webber page 275
//


	public class PeekableStack extends Stack {
		public String peek() {
			String s = remove();
			add(s);
			return s;
		}
}

// 	An alternate implementation

/*

public class PeekableStack extends Stack {
    public String peek() {
        return top.getData();
    }
}

*/
