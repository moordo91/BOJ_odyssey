#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int n = stoi(a);
    int m = stoi(b);

    int x = n + m;
    string y = to_string(x);
    reverse(y.begin(), y.end());
    x = stoi(y);
    cout << x << endl;

    return 0;
}
