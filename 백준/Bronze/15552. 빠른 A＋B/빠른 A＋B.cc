#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int a, b, t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    
}