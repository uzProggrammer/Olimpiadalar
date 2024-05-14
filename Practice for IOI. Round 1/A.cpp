#include <iostream>
#include <set>
#include <string>

using namespace std;

long long f(long long x) {
  set<char> digits;
  string str_x = to_string(x);
  for (char digit : str_x) {
    digits.insert(digit);
  }
  return digits.size();
}

long long g(long long x) {
  return f(x) * f(x) * x;
}

long long solve(long long L, long long R, long long MOD) {
  long long result = 0;
  for (long long x = L; x <= R; x++) {
    result = (result + g(x)) % MOD;
  }
  return result;
}

int main() {
  long long T;
  cin >> T;
  for (long long t = 0; t < T; t++) {
    long long L, R, MOD;
    cin >> L >> R >> MOD;
    long long result = solve(L, R, MOD);
    cout << result << endl;
  }

  return 0;
}