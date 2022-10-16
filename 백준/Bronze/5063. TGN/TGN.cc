#include <iostream>

using namespace std;

int main() {
	int t, a, b, c;
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		cin >> a >> b >> c;
		b -= c;

		if (a > b)
			cout << "do not advertise" << endl;
		else if (a < b)
			cout << "advertise" << endl;
		else
			cout << "does not matter" << endl;
	}	

	return 0;
}