#include <bits/stdc++.h>
using namespace std;

long long answer;

void merge_sort(vector<int>& arr, int start, int end) {
    if (start >= end) return;
    int mid = (start + end) / 2;

    merge_sort(arr, start, mid);
    merge_sort(arr, mid + 1, end);

    vector<int> temp(end - start + 1);
    int i = start, j = mid + 1, k = 0;

    while (i <= mid && j <= end) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            answer += (mid - i + 1);
        }
    }

    while (i <= mid) temp[k++] = arr[i++];
    while (j <= end) temp[k++] = arr[j++];

    for (int p = 0; p < temp.size(); p++) {
        arr[start + p] = temp[p];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) cin >> arr[i];

        answer = 0;
        merge_sort(arr, 0, n - 1);

        cout << answer << "\n";
    }
    return 0;
}
