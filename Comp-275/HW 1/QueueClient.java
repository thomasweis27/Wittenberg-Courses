import java.io.IOException;

public class QueueClient {
    public static void main(String[] args) throws IOException {
        String str="", opType="";
        new StdIn(new String[]{args[1]});
        while (!StdIn.isEmpty())
            str+=StdIn.readString()+" ";

        FixedCapacityArrayQueue queue;
        //enqueue operation
        if(args[0].equals("c")) {
            opType="Character";
            queue = new FixedCapacityArrayQueue(20);
            System.out.println("Size of queue before queue operation :"+queue.getLength());
            for (char ch:str.toCharArray()){
                if (ch!=' ')
                    queue.enqueue(String.valueOf(ch));
            }
        }
        else {
            opType="Word";
            String [] s= str.split(" ");
            queue = new  FixedCapacityArrayQueue(20);
            System.out.println("Size of queue before queue operation :"+queue.getLength());
            for (String w:s)
                queue.enqueue(w);
        }

        System.out.println("Queue state after enqueuing item as " +opType);
        queue.printQueue();
        //dequeue operation
        for (int i=0; i< Integer.parseInt(args[2]);i++){
            queue.dequeue();
        }
        System.out.println("Queue state after dequeuing item as " +opType);
        queue.printQueue();

    }
}
