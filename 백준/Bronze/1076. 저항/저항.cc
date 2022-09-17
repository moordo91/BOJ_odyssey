#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {
    string registers[10] = {
        "black", "brown", "red", 
        "orange", "yellow", "green", 
        "blue", "violet", "grey", "white"
    };

    long long ans;
    string color;
    int arr[3];
    double p;
    
    for (int i = 0; i < 3; i++) {
        cin >> color;
        for (int j = 0; j < 10; j++)
            if (color == registers[j])
                arr[i] = j;
    }

    ans = arr[0] * 10 + arr[1];
    p = pow(10, arr[2]);
    ans = ans * p;

    cout << ans << endl;

    return 0;
}