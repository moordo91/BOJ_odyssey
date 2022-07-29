#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int f = 1;
    for (int i = n; i > 0; i--)
        f *= i;
    
    printf("%d", f);
}