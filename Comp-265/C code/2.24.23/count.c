// Count.c Program

#include <stdio.h>

int count(){
     
    int n;  
    printf("\nEnter an integer: ");
    scanf("%d",&n);
	while (n > 0) {
		printf("\n n.address %x - n.value %d", &n, n );
		n--;
	}
	return 0;
}
