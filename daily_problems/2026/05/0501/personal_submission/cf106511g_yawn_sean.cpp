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

	vector<string> ans = {"", "A", "AB", "BAC", "BDCA", "CBEDA", "CFEDBA", "DCGFEBA", "DHGFECBA", "EDIHGFCBA", "EJIHGFDCBA", "FEKJIHGDCBA", "FLKJIHGEDCBA", "GFMLKJIHEDCBA", "GNMLKJIHFEDCBA", "HGONMLKJIFEDCBA", "HPONMLKJIGFEDCBA", "IHQPONMLKJGFEDCBA", "IRQPONMLKJHGFEDCBA", "JISRQPONMLKHGFEDCBA", "JTSRQPONMLKIHGFEDCBA", "KJUTSRQPONMLIHGFEDCBA", "KVUTSRQPONMLJIHGFEDCBA", "LKWVUTSRQPONMJIHGFEDCBA", "LXWVUTSRQPONMKJIHGFEDCBA", "MLYXWVUTSRQPONKJIHGFEDCBA", "MZYXWVUTSRQPONLKJIHGFEDCBA"};

	int t;
	cin >> t;

	while (t --) {
		int x;
		cin >> x;
		cout << ans[x] << '\n';
	}


	return 0;
}