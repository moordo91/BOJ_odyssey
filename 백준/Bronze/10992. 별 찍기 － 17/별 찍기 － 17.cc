#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n-1; i++)
        cout << " ";
    cout << "*" << endl;

    for (int i = 2; i < n; i++)
    {
        for (int j = n-i; j > 0; j--)
            cout << " ";
        cout << "*";
        for (int j = 0; j < (i-1)*2-1; j++)
            cout << " ";
        cout << "*" << endl;
    }
    for (int j = 0; n > 1 && j < 2*n-1; j++)
        cout << "*";
    cout << endl;
    
    return 0;
}