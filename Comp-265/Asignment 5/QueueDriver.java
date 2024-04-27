// Name: Thams Weis
// File: QueueDriver.java 
// Date: Spring 2023
// Desc: Implements Worklist interface example from Webber Text

//this was written on the paper of the asignment to make sure it works
public class QueueDriver{
    public static void main(String[] args) {

        Worklist w;
        w = new Queue(); 
        w.add("alpha");
        w.add("bravo");
        w.add("charlie");
        w.add("delta"); 
        w.add("easy");
        
        System.out.println("Begin");
        while (w.hasMore()) {
            System.out.println(w.remove());
        }
    System.out.println("End");
    }
}