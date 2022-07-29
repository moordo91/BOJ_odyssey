#include <iostream>
using namespace std;
int main()
{
    int n, k;
    int ans = 0;
    cin >> n;
    int arr[100];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cin >> k;
    for (int i = 0; i < n; i++) {
        if (arr[i] == k)
            ans++;
    }

    cout << ans;
}