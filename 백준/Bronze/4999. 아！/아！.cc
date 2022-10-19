#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string one, two;

	cin >> one >> two;
	
	if (one.size() >= two.size())
		cout << "go";
	else
		cout << "no";
}