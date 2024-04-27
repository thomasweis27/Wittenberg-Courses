//
// Name:
// File: SumArray.c
// Date: 02/24/2023
//
// Desc: Array Sum Demo Pgm 

#include <stdio.h>
#define MAXSIZE 20

int sumArray(int a[], int size){
	int i, sum = 0;
	for (i = 0; i< size; i++) {
		sum = sum + a[i];
		};
	printf("\n size.address = %x", &size);
	printf("\n a.address = %x", a);	
	return sum; 		
}
int SumMain(){
	
	int a[MAXSIZE], size = 0, i, sum ;
	
	printf("\nEnter number of item to input: ");
	scanf("%d",&size);
	printf("Enter %d integers\n",size);
	for (i = 0; i < size; i++){
		printf("?: ");
		scanf("%d",&a[i]);
	}    
	
    printf("\n size.address = %x", &size);
	printf("\n a.address = %x", a);	
	printf("\n i.address = %x", &i);
	printf("\n sum.address = %x",&sum);
	printf("\n");
	
	sum = sumArray(a, size);
	printf("\n\n Sum = %d\n",sum);
	
	return 0;
}
