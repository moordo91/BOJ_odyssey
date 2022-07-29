#include <iostream>
using namespace std;

int main()
{
    long long x, y;
    cin >> x >> y;

    if (x-y < 0)
        cout << y-x;
    else
        cout << x-y;
}