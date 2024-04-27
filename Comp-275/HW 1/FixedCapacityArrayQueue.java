import java.util.Arrays;

// class not renamed not has a scaleable capacity
public class FixedCapacityArrayQueue<T> {
    private T[] q;
    private int first=-1;
    private int last =-1;
    private int size=0; //denotes number of non-null items in the queue
    public FixedCapacityArrayQueue (int Capacity){
        q = (T[]) new Object[1]; 
    }
    public void enqueue(T item){
        if(q.length==size) {
            resize(q.length * 2);
        }
        q[++last] = item;
        size++;

    }

    public T  dequeue(){
        T item = null;
        if(!isEmpty()){
            item= q[++first];
            q[first]=null;
           if (size== q.length/4) {
               resize(q.length / 2 );
               first=-1;
           }
            size--;
            return item;
        }else{
            last=-1;
            first=-1;
            return null;
        }

    }

    public boolean isEmpty(){
        return size==0;
    }
       public void resize(int new_size){
       T [] temp =  (T[])  new Object [new_size];
       int j=0,i;
       for(i=0;i<q.length;i++){
           if (q[i] != null) {
               temp[j] = q[i];
               j++;
           };
       }
       q=temp;
   }

   public int size(){
        return size;
    }
    public int getLength(){
        return q.length;
    }
    public void printQueue(){

        System.out.print(Arrays.toString(q));
        System.out.println(":Size of queue is "+q.length);
    }

}
