#include <iostream>
using namespace std;
int main()
{
    int n, x;
    cin >> n >> x;
    int value;
    for (int i = 0; i < n; i++) {
        cin >> value;
        if (value < x)
            cout << value << " "; 
    }
}