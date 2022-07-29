#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int small(int a, int x)
{
	if (a < x)
	{
		printf("%d ", a);
	}
	return 0;
}


int main()
{
	int n, x, i, a;
	scanf("%d %d", &n, &x);
	for (i = 1; i <= n; i++)
	{
		scanf("%d", &a);
		small(a, x);
	}

	return 0;
}