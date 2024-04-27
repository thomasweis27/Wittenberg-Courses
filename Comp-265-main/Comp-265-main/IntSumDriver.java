import java.util.*;

public class IntSumDriver {

	static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args){
		int k, sum = 0;
		System.out.print("\nEnter an integer (0 to quit)\n?: ");
		k = scanner.nextInt();
		while (k != 0){
			sum += k;
			System.out.print("?: ");
			k = scanner.nextInt();
		}
	System.out.println("\nThe Sum = " + sum);
	}      //coersion - the plus in here makes the number part of the string
}  
