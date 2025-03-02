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

    if (i >= 1) {
      printf("The current sum is: %.1f, The current index is: %d\n", sum, i);
      average = (i == 1) ? sum / 2 : sum / i;
      printf("\nThe average is: %.1f\n", average);
    }
  }
}