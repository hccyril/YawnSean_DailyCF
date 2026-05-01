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

	int n;
	cin >> n;

	vector<int> v1(n), v2(n);
	for (auto &x: v1) cin >> x, x --;
	for (auto &x: v2) cin >> x, x --;

	auto find_cycles = [&] (vector<int> &perm) -> vector<int> {
		vector<int> vis(n, 0), possible(n + 1, 0);

		for (int i = 0; i < n; i ++) {
			if (!vis[i]) {
				int cur = i, cnt = 0;
				while (!vis[cur]) {
					vis[cur] = 1;
					cnt ++;
					cur = perm[cur];
				}
				possible[cnt] = 1;
			}
		}

		vector<int> ans;
		for (int i = 1; i <= n; i ++) {
			if (possible[i]) {
				ans.emplace_back(i);
			}
		}

		return ans;
	};

	auto w1 = find_cycles(v1);
	auto w2 = find_cycles(v2);

	long long ans = 0;

	for (auto &x: w1) {
		long long res = 1e18;
		for (auto &y: w2) {
			res = min(res, 1ll * x * y / gcd(x, y));
		}
		ans = max(ans, res);
	}

	cout << ans;

	return 0;
}