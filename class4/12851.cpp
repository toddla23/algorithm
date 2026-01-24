#include <iostream>
#include <deque>
#include <vector>
int INF = 1e9;
using namespace std;

void printVector(vector<int> v)
{
    for (int i = 0; i < 20; i++)
    {
        cout << v[i] << ", ";
    }
    cout << endl;
}
void calc(int n, int k, vector<int> &costs, vector<int> &answers)
{
    deque<int> toVisit;
    toVisit.push_back(n);
    int count = 0;
    while (!toVisit.empty())
    {
        int x = toVisit.front();
        toVisit.pop_front();
        vector<int> dx = {x + 1, x - 1, x * 2};
        for (int i = 0; i < 3; i++)
        {

            int t = dx[i];
            // cout << "_________________" << endl;
            // cout << "x: " << x << " t: " << t << endl;
            if (0 <= t && t <= 100000)
            {
                // cout << "x: " << x << " t: " << t << endl;

                if (costs[t] >= costs[x] + 1)
                {
                    if (costs[x] + 1 == costs[t])
                        answers[t] += answers[x];
                    else
                    {
                        answers[t] = answers[x];
                        costs[t] = costs[x] + 1;
                        toVisit.push_back(t);
                    }
                }
                // cout << t << " " << answers[t] << " " << costs[t] << endl;
            }
        }
    }
}

int main()
{
    vector<int> costs(100001, INF);
    vector<int> answers(100001, 0);
    // printVector(costs);
    // printVector(answers);

    int n, k;
    cin >> n >> k;
    costs[n] = 0;
    answers[n] = 1;
    calc(n, k, costs, answers);

    // printVector(costs);
    // printVector(answers);
    cout << costs[k] << endl
         << answers[k] << endl;
    return 0;
}