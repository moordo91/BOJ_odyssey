#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int x[100001];
int y[100001];

int compare(const void* a, const void* b) {
	int num1 = *(int*)a;
	int num2 = *(int*)b;

	if (num1 < num2) return -1;
	if (num1 > num2) return 1;
	return 0;
}

int binary_search(int list[], int n, int key) {
	int high, low, mid;
	low = 0;
	high = n - 1;
	while (low <= high) {
		mid = (low + high) / 2;
		if (key == list[mid]) return 1;
		else if (key > list[mid]) low = mid + 1;
		else high = mid - 1;
	}
	return 0;
}

int main() {
	int n, m, i, j;
	
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &x[i]);
	}

	qsort(x, n, sizeof(int), compare);

	scanf("%d", &m);

	for (i = 0; i < m; i++) {
		scanf("%d", &y[i]);
	}

	for (i = 0; i < m; i++) {
		printf("%d\n", binary_search(x, n, y[i]));
	}
	return 0;
}