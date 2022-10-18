#include <iostream>

using namespace std;

int main() {
	int n, sum=0;
	int a, s;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> s >> a;
		sum += a % s;
	}
	
	cout << sum << endl;

	return 0;
}