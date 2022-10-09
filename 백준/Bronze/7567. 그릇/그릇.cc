#include <iostream>
#include <string>

using namespace std;

int main()
{
    string bowl;
    int ans = 10;

    cin >> bowl;
    int n = bowl.size();

    for (int i = 1; i < n; i++)
    {
        if (bowl[i] != bowl[i-1])
            ans += 10;
        else
            ans += 5;
    }
    
    cout << ans << endl;
    return 0;
}