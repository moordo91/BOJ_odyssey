#include <iostream>
#include <string>

using namespace std;

int main() {
    string a, b, c, d;
    long long n1, n2;
    cin >> a >> b >> c >> d;

    a += b;
    c += d;

    n1 = stoll(a);
    n2 = stoll(c);

    cout << n1 + n2 << endl;

    return 0;
}