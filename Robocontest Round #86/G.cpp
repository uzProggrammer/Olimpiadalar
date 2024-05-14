#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
int last_total(vector<int> arr) {
    while (int(size(A)) > 1) {
        vector<int> new_array;
        for (int i = 0; i < size(A) - 1; i++) {
            new_array.push_back((A[i] + A[i + 1]) % MOD);
        }
        copy(new_array.begin(), new_array.end(), A.begin());
    }

    return A[0];
}
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int result = last_total(A);
    cout << result << endl;
    return 0;
}
