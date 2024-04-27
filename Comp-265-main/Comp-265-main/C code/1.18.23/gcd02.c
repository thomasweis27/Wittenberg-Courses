//
// Name:
// File: gcd02.c
//
//
#include <stdio.h>

 gcd(int a, int b){
 	int temp;
	while (a % b != 0){
		temp = a % b;
		a = b;
		b = temp;
	}
	return b;
}

int main1(){
	
	int a, b, c;
	
	printf("\nEnter two positive integers: ");
	scanf("%d %d",&a,&b); //& means addressed of a and b
	
	c = gcd(a,b);
	
	printf("\nThe gcd is %d\n",c);
	return 0;
}
