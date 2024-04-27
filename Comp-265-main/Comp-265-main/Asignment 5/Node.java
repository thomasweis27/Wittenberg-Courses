//most of this was from an example done in class
public class Node{
	private String data;
	private Node link;
		
	public Node(String theData, Node theLink) {
		data = theData;
		link = theLink;
	}

	public String getData() {
		return data;
	}
		//this was added my Thomas Weis to make the queue work
	public void setLink(Node link) {
        this.link = link;
    }
	
	public Node getLink() {
		return link;
	}
}
