#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
int n;
int h[100001];
pii p[100000];
ll acc[100001];

ll compute(int l, int r, int i, ll A) {
    if (acc[r - 1] - acc[l] <= A)
        return A;
    int m;
    for (int j = i; j < n; j++) {
        m = p[j].second;
        if (m > l && m < r) {
            i = j;
            break;
        }
    }
    A = max(A, (ll) p[i].first * (r - l - 1));
    A = compute(l, m, i, A);
    A = compute(m, r, i, A);
    return A;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> h[i];
        p[i - 1] = pii(h[i], i);
        acc[i] = acc[i - 1] + h[i];
    }
    sort(p, p + n);
    cout << compute(0, n + 1, 0, 0) << "\n";
}
