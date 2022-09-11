#include <iostream>
#define mod 1000000000

using namespace std;

int dp[101][10] = {0,};

int main() {

    int n, i, j, ans;
    cin >> n;
    for (i = 1; i < 10; i++)
        dp[1][i] = 1;

    for (i = 2; i <= n; i++) {
        for (j = 0; j < 10; j++) {
            if (j == 0)
                dp[i][0] = dp[i-1][j+1];
            else if (j == 9)
                dp[i][9] = dp[i-1][j-1];
            else
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];
            
            dp[i][j] %= mod;
        }
    }

    ans = 0;
    for (i = 0; i < 10; i++) {
        ans = (ans + dp[n][i]) % mod;
    }

    cout << ans << endl;

    return 0;
}