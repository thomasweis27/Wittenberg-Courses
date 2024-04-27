//
// Name:
// File: order02.c
//
//
#include <stdio.h>

order(int *a, int *b){ //the *a says a is an address(pointer) and not a value
 	int temp;
 	if (*a < *b) { //get what a points to and compare it to what b poins to
 	temp = *a;
 	*a = *b;
 	*b = temp;
	}
	return 0;
}

int main2(){
	
	int a, b;
	
	printf("\nEnter two positive integers: ");
	scanf("%d %d",&a,&b);
	
	order(&a, &b); //passing the addresses of a and b
	
	printf("\n %d > %d\n",a,b);
	return 0;
}
