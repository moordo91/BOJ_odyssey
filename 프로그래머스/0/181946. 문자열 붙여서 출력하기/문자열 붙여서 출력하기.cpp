#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void) {
    string str1, str2;
    cin >> str1 >> str2;
    string str;
    str = str1 + str2;
    str.erase(remove(str.begin(), str.end(), ' '), str.end());
    cout << str << endl;
    return 0;
}