#include <iostream>
using namespace std;

int main() {
    int sum, score, idx, max=0;
    for (int i = 0; i < 5; i++)
    {
        sum = 0;
        for (int j = 0; j < 4; j++)
        {
            cin >> score;
            sum += score;
        }
        
        if (max < sum)
        {
            idx = i + 1;
            max = sum;
        }
    }
    
    cout << idx << " " << max << endl;

    return 0;
}