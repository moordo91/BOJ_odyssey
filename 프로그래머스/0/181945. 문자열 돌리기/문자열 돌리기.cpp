#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    int i;
    int n = str.length();
    for (i = 0; i < n; i++) {
        cout << str[i] << endl;
    }
    return 0;
}