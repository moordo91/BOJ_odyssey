#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;

    for (int i = c; i > 0; i--)
    {
        if (2*b > a)
            b--;
        else
            a--;
    }

    cout << min(a/2, b) << endl;
    return 0;
}