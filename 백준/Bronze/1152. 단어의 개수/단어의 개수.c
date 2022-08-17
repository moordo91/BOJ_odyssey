#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int count_word(char* s)
{
	int i, wc = 0, waiting = 1;

	for (i = 0; s[i] != NULL; i++)
	{
		if (isalpha(s[i]))
		{
			if (waiting)
			{
				wc++;
				waiting = 0;
			}
		}
		else waiting = 1;
	}

	return wc;
}


int main()
{
	char str[1000000];
	gets(str);

	int wc = count_word(str);
	printf("%d", wc);

	return 0;
}
