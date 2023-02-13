#include <stdio.h>

int main() {
    int year;
    scanf("%d", &year);

    (year % 400 == 0) ? printf("1")
        : (year % 100 == 0) ? printf("0")
        : (year % 4 == 0) ? printf("1")
        : printf("0");

    return 0;
}