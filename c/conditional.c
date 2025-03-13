# include <stdio.h>

void main() {
    int a;
    int b; 

    printf("Digite um número: \n");
    scanf("%d", &a);

    printf("Digite um número: \n");
    scanf("%d", &b);

    if (a < b) {
        printf("%d %d \n", a, b);
    } else {
        printf("%d %d \n", b, a);
    }
}
