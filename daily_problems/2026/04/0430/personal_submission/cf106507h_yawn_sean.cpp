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

	int M = 1e6 + 5;
	vector<int> pr(M);
	iota(pr.begin(), pr.end(), 0);

	for (int i = 2; i < M; i ++) {
		if (pr[i] == i) {
			for (int j = i; j < M; j += i) {
				pr[j] = i;
			}
		}
	}

	int n, k;
	cin >> n >> k;

	vector<int> nums(n);
	for (auto &x: nums) cin >> x;

	vector<int> cnt(M, 0);

	for (auto x: nums) {
		while (x > 1) {
			cnt[pr[x]] ++;
			x /= pr[x];
		}
	}

	vector<int> dp(k + 1, 1);

	for (int i = 0; i < M; i ++) {
		if (cnt[i] >= n) {
			vector<int> pws(20, 0);

			for (auto &x: nums) {
				int pw = 0;
				while (x % i == 0) {
					x /= i;
					pw ++;
				}
				pws[pw] ++;
			}

			vector<pair<int, int>> transitions;
			int val = 1;

			for (int a = 1; a <= cnt[i] / n; a ++) {
				val *= i;
				int cost = 0;
				for (int b = 0; b < a; b ++)
					cost += (a - b) * pws[b];
				transitions.emplace_back(cost, val);
			}

			for (int i = k; i >= 0; i --) {
				int dp_val = dp[i];
				for (auto &[cost, val]: transitions) {
					if (i >= cost) {
						dp_val = max(dp_val, dp[i - cost] * val);
					}
				}
				dp[i] = dp_val;
			}
		}
	}

	for (int i = 1; i <= k; i ++) cout << dp[i] << ' ';

	return 0;
}