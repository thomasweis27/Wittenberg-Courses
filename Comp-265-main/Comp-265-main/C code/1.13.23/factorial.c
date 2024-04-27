#include <stdio.h>

 int factorial(){
   
   int n, k, fact;

   printf("\nEnter a positive integer n:");
   scanf("%d", &n);

   fact = 1; 
   for (k=1; k <n+1; k++){
     fact = fact *k;
   }

   printf("\n%d factorial = %d\n", n, fact);
   return 0;
 }