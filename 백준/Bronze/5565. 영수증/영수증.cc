#include <iostream>

using namespace std;

int main() {
    int cost, totalCost;
    cin >> totalCost;

    for (int i = 0; i < 9; i++)
    {
        cin >> cost;
        totalCost -= cost; 
    }
    cout << totalCost << endl;

    return 0;
}