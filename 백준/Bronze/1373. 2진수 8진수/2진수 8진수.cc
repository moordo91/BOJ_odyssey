#include <iostream>
#include <string>

using namespace std;

int main()
{
    string d2, d8;
    cin >> d2;

    int len = d2.size();
    int i = 0;
    if (len % 3 == 1) {
        cout << d2[0];
        i += 1;
    }
    else if (len % 3 == 2) {
        cout << ((d2[0]-'0')*2) + (d2[1]-'0');
        i += 2;
    }

    for (; i < len; i+=3)
    {
        cout << ((d2[i]-'0')*4) + ((d2[i+1]-'0')*2) + (d2[i+2]-'0');
    }

    cout << endl;
    
    return 0;
}