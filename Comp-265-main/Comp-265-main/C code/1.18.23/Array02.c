//
// Name:
// File: Array02.c
// Date: 01/18/2023
//
// Desc: Array Demo Pgm 

#include <stdio.h>
#define MAXSIZE 20

int array2(){
	
	int a[MAXSIZE], size = 0, i;
	int max, min; 
	
	// input to an array 
	
	printf("\nEnter number of item to input: ");
	scanf("%d",&size);
	printf("Enter %d integers\n",size);
	for (i = 0; i < size; i++){
		printf("?: ");
		scanf("%d",&a[i]);
	}    
	
	// processing an array 
		
	max = a[0];
	min = a[0];
	for (i = 0; i < size; i++){
		if (a[i] > max)
		   max = a[i];
		if (a[i] < min) 
		   min = a[i];  	
	}

	printf("\nMaximum = %d",max);
	printf("\nMinimum = %d",min);
	printf("\n");
	return 0;
}
