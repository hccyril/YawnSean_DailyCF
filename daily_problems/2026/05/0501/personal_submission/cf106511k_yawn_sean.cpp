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

	int k;
	cin >> k;

	vector<int> ans;

	for (int i = 0; i < 10000; i ++) {
		if (1ll * i * (i - 1) * (i - 2) / 6 > k) {
			i --;
			k -= 1ll * i * (i - 1) * (i - 2) / 6;
			while (i --) ans.emplace_back(0);
			break;
		}
	}

	int cur = 1;
	while (k) {
		int v = sqrt(k);
		if (v * v > k) v --;

		k -= v * v;
		ans.emplace_back(4 * cur);
		while (v --) {
			ans.emplace_back(-3 * cur);
			ans.emplace_back(-cur);
		}

		cur *= 10;
	}

	cout << ans.size() << '\n';
	for (auto &x: ans) cout << x << ' ';

	return 0;
}