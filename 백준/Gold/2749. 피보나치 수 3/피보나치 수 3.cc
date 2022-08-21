#include <iostream>
using namespace std;
const int mod = 1000000;
const int bnd = 1500000;

int dp[bnd] = {0,1};
int main() {
    long long n;
    cin >> n;
    for (int i=2; i<bnd; i++) {
        dp[i] = dp[i-1] + dp[i-2];
        dp[i] %= mod;
    }
    cout << dp[n%bnd] << '\n';
    return 0;
}