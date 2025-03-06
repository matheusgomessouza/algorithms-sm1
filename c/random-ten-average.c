#include <time.h>
#include <stdio.h>
#include <stdlib.h>

int i;
float sum;
float average;

void main() {
    srand(time(NULL));

    for (i = 0; i < 10; i++) {
      int number = rand();
      sum += number;
      printf("The current value of sum is: %.1f\n", sum);
  }

  average = sum / 10;
  printf("The average is: %.1f\n", average);
}