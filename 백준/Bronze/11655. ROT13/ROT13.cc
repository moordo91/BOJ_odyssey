#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    getline(cin, s);

    for (int i = 0; i < s.size(); i++) {
        if ((65 <= s[i] && s[i] < 78) || (97 <= s[i] && s[i] < 110)) {
            s[i] += 13;
        }
        else if ((78 <= s[i] && s[i] < 91) || (110 <= s[i] && s[i] < 123)) {
            s[i] -= 13;
        }
    }
    
    cout << s << endl;

    return 0;
}