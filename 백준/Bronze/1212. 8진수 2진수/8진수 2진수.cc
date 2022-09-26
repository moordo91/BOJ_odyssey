#include <iostream>
#include <string>
using namespace std;

string eightToTwo(string base8) {
    string base2 = "";
    int n = base8.size();

    for (int i = 0; i < n; i++)
    {
        switch (base8[i]) {
            case '1':
                base2 += "001";
                break;
            case '2':
                base2 += "010";
                break;
            case '3':
                base2 += "011";
                break;
            case '4':
                base2 += "100";
                break;
            case '5':
                base2 += "101";
                break;
            case '6':
                base2 += "110";
                break;
            case '7':
                base2 += "111";
                break;
            default:
                base2 += "000";
        }
    }

    while (true)
    {
        if ((base2[0] == '0') && (base2.size() > 1))
            base2 = base2.substr(1, 3*n-1);
        else
            break;
    }
    return base2;
}

int main() {
    string base8;
    cin >> base8;

    cout << eightToTwo(base8) << endl;

    return 0;
}