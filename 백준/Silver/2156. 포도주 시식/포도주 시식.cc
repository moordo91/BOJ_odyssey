#include <iostream>
#include <algorithm>
using namespace std;

int arr[10000];
int dp[10001];

int main() {
    int n, i, ans;
    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> arr[i];
    }

    dp[0] = arr[0];
    dp[1] = dp[0] + arr[1];
    dp[2] = max({dp[1], arr[0]+arr[2], arr[1]+arr[2]});

    for (i = 3; i < n; i++) {
        dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]);
        dp[i] = max(dp[i], dp[i-1]);
    }


    cout << dp[n-1] << endl;
    return 0;
}