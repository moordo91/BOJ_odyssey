#include <iostream>
using namespace std;

int main() {
    int arr[1002] = {0, };
    int a, b;
    int n = 1;
    int i = 0;
    int sum = 0;

    cin >> a >> b;

    while (true) {
        if (arr[1000] != 0)
            break;

        for (int j = 0; j < i; j++) {
            if (arr[1000] != 0)
               break;
            arr[n] = i;
            n++;
        }
        i++;
    }
    
    for (int j = a; j <= b; j++)
        sum += arr[j];

    cout << sum << endl;

    return 0;
}