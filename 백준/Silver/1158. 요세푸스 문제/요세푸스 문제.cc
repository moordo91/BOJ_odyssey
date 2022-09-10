#include <iostream>
#include <queue>
using namespace std;

int main() {
    int i, n, k;
    cin >> n >> k;
    queue<int> q;

    for (i = 1; i <= n; i++)
        q.push(i);

    cout << '<';
    while (true) {
        for (i = 0; i < k-1; i++) {
            q.push(q.front());
            q.pop();
        }

        cout << q.front();
        q.pop();

        if (!q.size()) {
            break;
        }

        cout << ", ";

    }
    cout << '>' << endl;
    
    return 0;
}