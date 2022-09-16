#include <iostream>
using namespace std;

int main() {

    int a, b, i;
    cin >> a >> b;

    a = a - a % 100;
    i = a;

    while (true) {
        if (i % b == 0) {
            if (i % 100 < 10)
                cout << "0";
            cout << i % 100;
            break;
        }
        i++;
    }
    return 0;
}