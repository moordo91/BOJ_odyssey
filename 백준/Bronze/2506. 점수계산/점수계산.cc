#include <iostream>

using namespace std;

int main() {
    int arr[100] = {0,};
    int n, score=1, ans=0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 0)
            score = 1;
        else {
            ans += score;
            score++;
        }
    }
    
    cout << ans << endl;

    return 0;
}