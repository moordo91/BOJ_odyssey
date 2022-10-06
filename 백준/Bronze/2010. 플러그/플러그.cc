#include <iostream>

using namespace std;

int main()
{
    int n, temp, sum=0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        sum += temp;
    }

    sum -= n-1;

    cout << sum << endl;
    
    return 0;
}