#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    int m, n, i, sum=0;
    cin >> m >> n;
    i = sqrt(m);

    while (i*i <= n)
    {
        if (i*i >= m)
            q.push(i*i);
        i++;
    }

    int min = q.front();

    if (!q.size())
        cout << -1 << endl;

    else {
        while (q.size())
        {
            sum += q.front();
            q.pop();
        }

        cout << sum << endl
             << min << endl;
    }

    return 0;
}