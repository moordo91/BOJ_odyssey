#include <iostream>
#define MAX 1000000000

using namespace std;

int N;
int arr[11];
int oper[4];

int maxVal = -MAX;
int minVal = MAX;

void sol(int result, int idx) {
    
    if (idx == N) {
        if (result < minVal)
            minVal = result;
        if (result > maxVal)
            maxVal = result;
        return;
    }

    for (int i = 0; i < 4; i++) {

        if (oper[i] > 0) {
            oper[i]--;
            if (i == 0)
                sol(result + arr[idx], idx+1);
            else if (i == 1)
                sol(result - arr[idx], idx+1);
            else if (i == 2)
                sol(result * arr[idx], idx+1);
            else
                sol(result / arr[idx], idx+1);
            oper[i]++;
        }
    }
    return; 
}

int main() {
    
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> arr[i];

    for (int i = 0; i < 4; i++)
        cin >> oper[i];

    sol(arr[0], 1);
    cout << maxVal << endl
         << minVal << endl;

    return 0;
}
