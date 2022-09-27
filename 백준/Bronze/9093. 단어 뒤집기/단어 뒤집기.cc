#include <iostream>
#include <string>
#include <stack>

using namespace std;

void reverseString(string str);

int main() {
    int t;
    cin >> t;
    cin.ignore();

    for (int i = 0; i < t; i++)
    {
        string str;
        getline(cin, str);
        str += ' ';
        reverseString(str);
    }
    return 0;
}

void reverseString(string str) {
    stack<char> stk;
    
    for (char ch : str)
    {
        if (ch == ' ')
        {
            while (!stk.empty())
            {
                cout << stk.top();
                stk.pop();
            }
            cout << ch;
        }
        else
            stk.push(ch);
    }
    cout << endl;
}