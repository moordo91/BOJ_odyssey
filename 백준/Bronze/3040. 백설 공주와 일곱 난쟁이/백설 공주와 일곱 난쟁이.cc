#include <iostream>

using namespace std;

int main() {
	int arr[9];
	int sum = 0;
	int a, b;

	for (int i = 0; i < 9; i++)
	{
		cin >> arr[i];
		sum += arr[i];
	}

	for (int i = 0; i < 8; i++)
	{	
		sum -= arr[i];
		for (int j = i+1; j < 9; j++)
		{
			sum -= arr[j];
			if (sum == 100) {
				arr[i] = -1;
				arr[j] = -1;
			}
			sum += arr[j];
		}
		sum += arr[i];
	}

	for (int i = 0; i < 9; i++)
	{
		if (arr[i] >= 0)
			cout << arr[i] << endl;
	}
}