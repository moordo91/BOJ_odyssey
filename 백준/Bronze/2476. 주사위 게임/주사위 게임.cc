#include <iostream>
#include <algorithm>

using namespace std;

int sol(int a, int b, int c) {
    if (a == b && b == c)
        return 10000 + a * 1000;
    else if (a == b)
        return 1000 + a * 100;
    else if (b == c)
        return 1000 + b * 100;
    else if (c == a)
        return 1000 + c * 100;
    else
        return max(max(a, b), c) * 100;
}

int main() {
    int a, b, c, t, max=0;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> a >> b >> c;
        if (max < sol(a, b, c))
            max = sol(a, b, c);
    }

    cout << max << endl;
    
    return 0;
}
