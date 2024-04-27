#include <stdio.h> 

int test() {

  int n,k,i;

  printf("Enter a positive integer> 1: "); // ask for user input
  scanf("%d", &n);
  k= 2;
  L1: 
  if (n <=1) goto L2;
  if (n%k ==0) goto L3;   
      k++; 
      goto L1;
  L3:
    printf("\nPrime divisors: %d", k);
    n = n/k;
    goto L1;
  L2:  printf("\nDone");
}