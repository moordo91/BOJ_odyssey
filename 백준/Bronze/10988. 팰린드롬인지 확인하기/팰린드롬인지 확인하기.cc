#include <iostream>
#include <string>
using namespace std;

int main() {
    string word;
    cin >> word;
    int n = word.size();
    int swtch = 1;

    if (n % 2 == 0) {
        for (int i = 0; i <= n/2; i++)
        {
            if (word[i] != word[n-1-i]) {
                swtch = 0;
                break;
            }
        }
    }
    else {
        for (int i = 0; i < n/2; i++)
        {
            if (word[i] != word[n-1-i]) {
                swtch = 0;
                break;
            }    
        }
    }
    cout << swtch << endl;
    return 0;
}