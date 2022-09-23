#include <iostream>
using namespace std;

int main()
{
    int n, m, h, i, j, k, a, b, x, y, sum;
    int arr[300][300];

    cin >> n >> m;

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            cin >> arr[i][j];
        }
    }

    cin >> k;

    for (h = 0; h < k; h++)
    {
        sum = 0;
        cin >> a >> b >> x >> y;

        a -= 1;
        b -= 1;
        x -= 1;
        y -= 1;

        for (i = 0; i < x - a + 1; i++)
        {
            for (j = 0; j < y - b + 1; j++)
            {
                sum += arr[a + i][b + j];
            }
        }
        cout << sum << endl;
    }

    return 0;
}