#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

queue<int> q;

int main() {
    int n;

    for (int i = 0; i < 7; i++)
    {
        cin >> n;
        if (n % 2 == 1) {
            q.push(n);
        }
    }

    if (!q.size()) {
        cout << -1 << endl;
        return 0;
    }

    int minOdd = 1000000000;
    int sum = 0;
    int cnt = q.size();


    for (int i = 0; i < cnt; i++)
    {   
        n = q.front();
        q.pop();
        if (n < minOdd)
            minOdd = n;
        sum += n;
    }
    
    cout << sum << endl
         << minOdd << endl;
    
    return 0;
}