// we are working in c (.c) not c++ (.cpp)

#include <stdio.h>

int notes(void) {
  printf("Hello World\n");
  return 0;


//in c, we have to declare that "a" is an it and cannot change the type
  int a, b, c;
  a = 2; 
  b = 3; 
  c = a + b;
  //"elif" = "else if" in C
  printf(c);
  //scanf(" <format> ", &var list);
}