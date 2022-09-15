#include <iostream>
#include <algorithm>

using namespace std;


int main() {
    int arr[16][2] = {0, };
    int dp[15] = {0, };
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> arr[i][0] >> arr[i][1];
    }
    
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[i][0] + i <= n+1 && arr[j][0] + j <= i)
            {
                dp[i] = max(dp[i], dp[j] + arr[i][1]);
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; i++)
    {
        ans = max(ans, dp[i]);
    }
    
    cout << ans << endl;

    return 0;
}