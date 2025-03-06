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

    if (i >= 1) {
      printf("The current sum is: %.1f, The current index is: %d\n", sum, i);
      average = (i == 1) ? sum / 2 : sum / i;
      printf("\nThe average is: %.1f\n", average);
    }
  }
}