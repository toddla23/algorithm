#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll merge_count(vector<int> &arr, int l, int r) {
    if (r - l <= 1) return 0;
    int m = (l + r) / 2;
    ll inv = 0;
    inv += merge_count(arr, l, m);
    inv += merge_count(arr, m, r);

    vector<int> tmp;
    tmp.reserve(r - l);

    int i = l, j = m;
    while (i < m && j < r) {
        if (arr[i] <= arr[j]) {
            tmp.push_back(arr[i++]);
        } else {
            tmp.push_back(arr[j++]);
            inv += (m - i); // 왼쪽 잔여 원소 개수 = 역전쌍
        }
    }
    while (i < m) tmp.push_back(arr[i++]);
    while (j < r) tmp.push_back(arr[j++]);

    copy(tmp.begin(), tmp.end(), arr.begin() + l);
    return inv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;

        vector<int> A(N), B(N), pos(N+1);
        for (int i = 0; i < N; i++) {
            cin >> A[i];
            pos[A[i]] = i + 1; // A에서의 위치 (1-based)
        }
        for (int i = 0; i < N; i++) {
            cin >> B[i];
            B[i] = pos[B[i]]; // B를 A의 좌표계로 변환
        }

        ll ans = merge_count(B, 0, N);
        cout << ans << "\n";
    }
}
