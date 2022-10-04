#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s[5];
    for (int i = 0; i < 5; i++)
    {
        cin >> s[i];
    }
    for (int i = 0; i < 15; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (s[j].size() <= i)
                continue;
            cout << s[j][i];
        }
    }
    cout << '\n';
    return 0;
}