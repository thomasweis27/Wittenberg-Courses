//
// Name:
// File: Array01.c
// Date: 01/18/2023
//
// Desc: Array Demo Pgm 

#include <stdio.h>
#define MAXSIZE 20 
//the length or the array 20

int array1(){
	
	int a[MAXSIZE], size = 0, i;
  //need another variable to keep track of position in array
	
	printf("\nEnter number of item to input: ");
	scanf("%d",&size);
	printf("Enter %d integers\n",size);
	for (i = 0; i < size; i++){
		printf("?: ");
		scanf("%d",&a[i]);
	}    
	
	printf("The integers in reverse order are\n");
	for (i = size -1; i >= 0;i--){
		printf("%d\n",a[i]);
	}
	
	
	return 0;
}
