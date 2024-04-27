// Factorial Program

#include <stdio.h>

int f(int n){
    printf("\n n.address = %x n.value = %d",&n, n);
    if (n ==1) 
	    return 1;
    else 
	    return( n * f(n-1));
}

int factorial(){
    int n, m; 
    printf("\nEnter an integer: ");
	scanf("%d",&n);
	printf("\n n.address = %x n.value = %d\n",&n, n);
	
	m = f(n);
	printf("\n\n %d factorial = %d m.address = %x ",n, m, &m);
	return 0;
}
