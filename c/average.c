#include <stdio.h>

int main() {
  printf("Type the first number:");
  int numberOne;
  scanf("%d", &numberOne);
  printf("Type the second number:");
  int numberTwo;
  scanf("%d", &numberTwo);

  int average = (numberOne + numberTwo) / 2;
  printf("The average is: %d\n", average);
}