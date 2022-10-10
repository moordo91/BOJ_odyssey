#include <iostream>
#include <string>

using namespace std;

int main()
{
    int sum=0, max=0, a, b;
    for (int i = 0; i < 10; i++)
    {
        cin >> a >> b;
        sum += b - a;
        if (sum > max)
            max = sum;
    }

    cout << max << endl;
    
    return 0;
}