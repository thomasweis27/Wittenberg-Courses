//
// Name:
// File: Pointer01.c
// Date:
//
// Desc:

#include <stdio.h>
#include <stdlib.h>

int main3(){

	int *p; // pointer veriable - the position of the int - allocates memory for an int	
	int n = sizeof(int); //builtin function to look at computer bytes and allocates the approperate amount of code; 32 bytes --> 4 byes allocated, 64 --> 8 bytes allocated
	
	p = malloc(n); // allocate memroy for an int
	printf("\nEnter an integer: ");
	scanf("%d",p);   // note the pointer type parameter
	
	printf("\nEcho: %d : address 0x%x\n",*p,p); // %x is hex field
              // *p = what p points to, p = the actual address
	
	return 0;
}
