/*
哪些不用动？哪些必须动？
考虑一个上升子序列，数字的大小是连续的，则这个子序列里所有的元素都不需要动，只需要动其他的即可
其他数一定要动吗？是的，因为每次都得往最左或者最右拿，导致大小顺序也改变
2 3 8 5 4 6 7 1，2 3 4 是最长连续上升的，1 往左拿，5 6 7 8 必须往右拿
*/

int n, a[N], dp[N];

void meibao() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    int res = 0;
    for (int i = 1; i <= n; i++) {
        dp[a[i]] = dp[a[i] - 1] + 1;
        res = max(res, dp[a[i]]);
    }
    cout << n - res << "\n";
}
