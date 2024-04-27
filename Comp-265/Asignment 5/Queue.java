//
// Name:Thomas Weis
// File: Queue.java
// Date: Spring 2023
//
// Desc: Implements queue based off of a stack program talked about in class. 
//

public class Queue implements Worklist {
    private Node head = null;
    private Node tail = null;

    public void add(String data) {
        Node newNode = new Node(data, null);

        //end case
        if (tail != null) {tail.setLink(newNode);}
        tail = newNode;

        //exchange the head and tail
        if (head == null) {head = tail;}
    }
    //applies the has more function from the QueueDrive.java
    public boolean hasMore() {return (head != null);}

    public String remove() {
    Node n = head;
    head = n.getLink();

    if (head == null) {tail = null;}

    return n.getData();
    }
}
