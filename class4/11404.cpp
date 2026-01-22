#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

void printMatrix(vector<vector<int>> m)
{
    int s = m.size();

    for (int i = 0; i < s; i++)
    {
        for (int j = 0; j < s; j++)
        {
            if (m[i][j] == INF)
            {
                cout << 0 << " ";
            }
            else
            {
                cout << m[i][j] << " ";
            }
        }
        cout << endl;
    }
}
int main()
{
    int n, m;
    cin >> n;
    cin >> m;
    vector<vector<int>> answers(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++)
    {
        answers[i][i] = 0;
    }
    for (int i = 0; i < m; i++)
    {
        int start, end, cost;
        cin >> start >> end >> cost;
        if (answers[start - 1][end - 1] > cost)
            answers[start - 1][end - 1] = cost;
    }

    // printMatrix(answers);

    for (int i = 0; i < n; i++)
    { // 거쳐갈거
        for (int j = 0; j < n; j++)
        { // 시작점
            for (int k = 0; k < n; k++)
            { // 끝점
                int tempCost = answers[j][i] + answers[i][k];
                if (tempCost < answers[j][k])
                {
                    answers[j][k] = tempCost;
                }
            }
        }
    }

    printMatrix(answers);

    return 0;
}