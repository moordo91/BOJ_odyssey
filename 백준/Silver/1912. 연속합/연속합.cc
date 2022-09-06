#include <iostream>
#include <algorithm>

using namespace std;

int arr[100000];
int dp[100000];

int main()
{
    int n, ans;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    ans = arr[0];
    dp[0] = arr[0];

    for (int i = 1; i < n; i++)
    {
        dp[i] = max(arr[i], dp[i-1]+arr[i]);
        ans = max(dp[i], ans);
    }

    cout << ans << endl;

    return 0;
}