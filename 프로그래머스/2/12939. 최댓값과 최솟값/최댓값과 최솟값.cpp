#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>

using namespace std;

string solution(string s) {
    stringstream ss(s);
    vector<int> numbers{istream_iterator<int>{ss}, istream_iterator<int>{}};
    auto [min_it, max_it] = minmax_element(numbers.begin(), numbers.end());
    string answer = to_string(*min_it) + " " + to_string(*max_it);
    return answer;
}