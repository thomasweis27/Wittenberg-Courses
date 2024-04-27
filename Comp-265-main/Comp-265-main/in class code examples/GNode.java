//
// File: GNode.java
//
// Desc: See Webber page 286
//
	public class GNode<T> {
		private T data;
		private GNode<T> link;
		public GNode(T theData, GNode<T> theLink) {
			data = theData;
			link = theLink;
		}
		public T getData() {
			return data;
		}
		public GNode<T> getLink() {
			return link;
		}
	}