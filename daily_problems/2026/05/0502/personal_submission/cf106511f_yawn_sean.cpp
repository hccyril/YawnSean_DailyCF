#include <bits/stdc++.h>
// #pragma GCC optimize("O3,Ofast,unroll-loops")
// #include "atcoder/all"

using namespace std;
auto rng = mt19937(random_device()());
auto rngl = mt19937_64(random_device()());

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int t;
	cin >> t;

	while (t --) {
		int x, y;
		cin >> x >> y;

		if (x == 1 && y == 1) cout << 1;
		else if (x == 1 || y == 1) cout << 2;
		else if (x != y) cout << 4;
		else cout << 8;

		cout << '\n';
	}

	return 0;
}