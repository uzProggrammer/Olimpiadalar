#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;

    vector<long long> d2;
    for (long long i = 0; i < b; i++) {
        long long e, d1;
        cin >> e >> d1;
        d2.push_back(d1);
    }

    long long q;
    cin >> q;

    vector<string> s;
    long long maxDist = 0;
    for (long long i = 0; i < q; i++) {
        char t;
        string y;
        cin >> t >> y;

        if (t == '+') {
            s.push_back(y);
        } else {
            s.erase(remove(s.begin(), s.end(), y), s.end());
        }

        if (s.size() == 1) {
            cout << 0 << endl;
            maxDist = 0;
        } else if (s.empty()) {
            cout << -1 << endl;
            maxDist = 0;
        } else {
            long long index = find(d2.begin(), d2.end(), stoi(y)) - d2.begin();
            long long dist = index + 1;
            if (maxDist < dist) {
                maxDist = dist;
                cout << dist << endl;
            } else {
                cout << maxDist << endl;
            }
        }
    }

    return 0;
}
