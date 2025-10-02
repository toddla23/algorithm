#include <bits/stdc++.h>
using namespace std;

// 입력 배열: Bolts, Nuts
// Bolts-Bolts/Nuts-Nuts 비교는 할 수 없음
vector<int> Bolts, Nuts;
// 볼트와 너트의 비교: Bolts[i] vs Nuts[j]
// 반환값:
// (1) -1 if Bolts[i] < Nuts[j]
// (2) 0 if Bolts[i] == Nuts[j]
// (3) +1 if Bolts[i] > Nuts[j]
int CmpBoltNut(int i, int j)
{
    if (Bolts[i] < Nuts[j])
        return -1;
    if (Bolts[i] > Nuts[j])
        return +1;
    return 0;
}

void swapArr(vector<int> &arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void calc(vector<int> &bolts, vector<int> &nuts, int low, int high, vector<int> &boltNum, vector<int> &nutNum)
{
    if (low >= high)
        return;

    int j = low;
    int target = low;

    for (int i = low; i <= high; i++)
    {
        if (CmpBoltNut(low, i) == 0)
        {
            target = i;
        }
        if (CmpBoltNut(low, i) >= 0)
        {
            swapArr(Nuts, i, j);
            swapArr(nutNum, i, j);
            if (Bolts[low] == nuts[j])
            {
                target = j;
            }
            j++;
        }
    }
    j--;

    swapArr(Nuts, target, j);
    swapArr(nutNum, target, j);
    int k = low;

    for (int i = low; i <= high; i++)
    {
        if (CmpBoltNut(i, j) == 0)
        {
            target = i;
        }
        if (CmpBoltNut(i, j) <= 0)
        {
            swapArr(Bolts, i, k);
            swapArr(boltNum, i, k);
            if (Bolts[k] == nuts[j])
            {
                target = k;
            }
            k++;
        }
    }
    k--;
    swapArr(Bolts, target, k);
    swapArr(boltNum, target, k);
    calc(Bolts, Nuts, low, j - 1, boltNum, nutNum);
    calc(Bolts, Nuts, j + 1, high, boltNum, nutNum);
    return;
}

int main()
{
    int num_test_cases;
    cin >> num_test_cases;
    while (num_test_cases--)
    {
        int n; // 볼와 너트의 개수
        cin >> n;
        vector<int> boltNum(n + 1);
        vector<int> nutNum(n + 1);
        Bolts.assign(n + 1, 0);
        Nuts.assign(n + 1, 0);
        for (int i = 1; i <= n; ++i)
        {
            boltNum[i] = i;
            cin >> Bolts[i];
        }
        for (int j = 1; j <= n; ++j)
        {
            nutNum[j] = j;
            cin >> Nuts[j];
        }
        // 볼트와 너트 문제 해결 알고리즘
        // 볼트와 너트의 크기를 비교하기 위해 함수 CmpBoltNut 를 호출해야 함
        // 다음과 같이 볼트끼리 혹은 너트끼리 비교할 수 없음
        // if (Bolts[i] == Bolts[j]) 비교 불가능함
        // if (Nuts[i] == Nuts[j]) 비교 불가능함
        calc(Bolts, Nuts, 0, n, boltNum, nutNum);
        vector<int> answer(n + 1);
        for (int i = 0; i < boltNum.size(); i++)
        {
            answer[boltNum[i]] = nutNum[i];
        }
        // cout << "answer"<<endl;
        for (int i = 1; i < answer.size(); i++)
        {
            cout << answer[i]<< " ";
        }
        cout<<endl;
    }
    return 0;
}