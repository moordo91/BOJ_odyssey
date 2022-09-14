#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N;
int arrA[50];
int arrB[50];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> arrA[i];
    for (int i = 0; i < N; i++)
        cin >> arrB[i];

    sort(arrA, arrA+N);
    sort(arrB, arrB+N, greater<>());

    int sum = 0;
    for (int i = 0; i < N; i++)
        sum += arrA[i] * arrB[i];
    
    cout << sum << endl;

    return 0;
}