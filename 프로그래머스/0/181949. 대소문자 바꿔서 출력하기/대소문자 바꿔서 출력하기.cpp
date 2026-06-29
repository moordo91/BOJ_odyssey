#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    int tolower = 'a' - 'A';
    int toupper = 'A' - 'a';
    cin >> str;
    int n = str.length();
    for (int i = 0; i < n; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            cout << static_cast<char>(str[i] + tolower);
        } else {
            cout << static_cast<char>(str[i] + toupper);
        }
    }
    return 0;
}