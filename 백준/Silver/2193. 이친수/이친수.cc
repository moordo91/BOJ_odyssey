#include <iostream>

using namespace std;

long long fib[91] = {0, 1, 1, 0,};

int main() {
    int i, n;
    cin >> n;

    for (i = 3; i < 91; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }

    cout << fib[n] << endl;

    return 0;
}