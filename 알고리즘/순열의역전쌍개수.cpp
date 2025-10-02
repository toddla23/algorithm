#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int answer = 0;
void mearge(vector<int> &arr, int start, int mid, int end)
{
    int a = start;
    int b = mid + 1;
    int t = 0;

    // cout << "start: " << start << ", mid: " << mid << ", end: " << end << endl;

    vector<int> temp(end - start + 1);

    while (a <= mid && b <= end)
    {
        if (arr[a] <= arr[b])
        {
            temp[t] = arr[a];
            a++;
            t++;
        }
        else
        {
            temp[t] = arr[b];
            b += 1;
            t += 1;
            answer = answer + mid + 1 - a;
        }
    }
    while (a <= mid)
    {
        temp[t] = arr[a];
        a++;
        t++;
    }
    while (b <= end)
    {
        temp[t] = arr[b];
        b++;
        t++;
    }

    for (int p = 0; p < temp.size(); p++)
    {
        arr[start + p] = temp[p];
    }
    // cout << "answer: " << answer << endl;
    // for (int v : arr)
    //     cout << v << " ";
    // cout << endl;

    return;
}

void calc(vector<int> &arr, int start, int end)
{
    int mid = (start + end) / 2;
    if (end - start == 0)
    {
        return;
    }

    calc(arr, start, mid);
    calc(arr, mid + 1, end);
    mearge(arr, start, mid, end);
    return;
}

int main(void)
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        answer = 0;
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int j = 0; j < n; j++)
        {
            cin >> arr[j];
        }

        calc(arr, 0, n - 1);

        cout << answer << endl;
    }

    return 0;
}