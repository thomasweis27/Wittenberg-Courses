//
// Name:
// File: DynamicArray.c
// Date: 01/18/2023
//
// Desc: A dynamoc array of int
//
#include <stdio.h>
#include <stdlib.h>

//basically the same as stacks (push and pop) from 255. 
int dynamicarray(){
	
	struct inode {
		int data; 
		struct inode *link}; //structure has two fields, an object and a pointer
	struct inode *p = NULL, *q; //initally p is empty before filling it up
	int k, inodeSize = sizeof(struct inode);
	int max, min;
	
	// input list 
	
	printf("\nEnter an integer\n");
	printf("?: ");
	scanf("%d",&k);
	while (k != 0){
		q = malloc(inodeSize);
		q->data = k; //means q points to datafield
		q->link = p; //means q points to the link
		p = q;
		printf("Address =0x%x\n",p);
		printf("?: ");
		scanf("%d",&k);
	}
		
	// Find Maximum
	
	max = p->data;
	min = p->data;
	q = p;
	while (q != NULL){
		if (q->data > max)
		    max = q->data;
		if (q->data < min)
		    min = q->data;    
		q = q->link;  // chain down the list 
	}

	printf("\nMaximum = %d",max);
	printf("\nMinimum = %d",min);	
	
	// display list
		
	printf("\nDisplay List\n");
	while (p != NULL){
		printf("%d\n",p->data);
		q = p;
		p = p->link;
		free(q); // deallocate memory
	}	
		
		printf("\nEnd of Program\n");
		return 0;
			
	
}
	
