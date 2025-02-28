#include <stdio.h>

int i;
float sum;
float average;

void main() {
  for (i = 0; i < 10; i++) {
    printf("Type a number: ");
    int number;
    scanf("%d", &number);

    sum += number;
  }

  average = sum / 10;
  printf("The average is: %.1f\n", average);
}