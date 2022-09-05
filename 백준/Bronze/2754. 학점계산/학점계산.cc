#include <iostream>
#include <string.h>
using namespace std;

int main() {
    string grade;
    cin >> grade;

    double ans = 0;
    cout << fixed;
    cout.precision(1);
    
    switch (grade[0]) {
        case 'A':
            ans += 4.0;
            break;
        case 'B':
            ans += 3.0;
            break;
        case 'C':
            ans += 2.0;
            break;
        case 'D':
            ans += 1.0;
            break;
    }

    switch (grade[1]) {
        case '+':
            ans += 0.3;
            break;
        case '-':
            ans -= 0.3;
            break;
    }

    cout << ans << endl;

    return 0;
}