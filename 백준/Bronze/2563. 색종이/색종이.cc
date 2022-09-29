#include <iostream>
using namespace std;

int main()
{
    bool paper[100][100] = {false, };
    int n, cnt=0;
    cin >> n;
    
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
    
        for (int i = a; i < a+10; i++)
            for (int j = b; j < b+10; j++)
                paper[i][j] = true;
    }

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++)
            if (paper[i][j])
                cnt++;
    }
    
    cout << cnt << endl; 
    return 0;
}