#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

vector<vector<int>> multipleMatrix(vector<vector<int>> m1, vector<vector<int>> m2)
{
    vector<vector<int>> answer;
    int s = m1.size();
    for (int i = 0; i < s; i++)
    {
        vector<int> temp;
        for (int j = 0; j < s; j++)
        {
            int a = 0;
            for (int k = 0; k < s; k++)
            {
                a = a + m1[i][k] * m2[k][j];
            }
            temp.push_back(a % 1000);
        }
        answer.push_back(temp);
    }
    return answer;
}

void printMatrix(vector<vector<int>> m)
{
    int s = m.size();

    for (int i = 0; i < s; i++)
    {
        for (int j = 0; j < s; j++)
        {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{

    int n;
    long long b;

    cin >> n >> b;
    // cout << n << " "<< b << endl;

    vector<vector<int>> t;
    for (int i = 0; i < n; i++)
    {
        vector<int> temp;
        int x;
        for (int j = 0; j < n; j++)
        {
            cin >> x;
            temp.push_back(x);
        }
        t.push_back(temp);
    }

    bitset<64> decimal_to_binary(b);
    string binary_string = decimal_to_binary.to_string();

    size_t first_found = binary_string.find('1');

    if (first_found != string::npos)
    {
        binary_string = binary_string.substr(first_found);
    }
    vector<vector<vector<int>>> calcs(binary_string.size());
    calcs[0] = t;

    for (int i = 1; i < binary_string.size(); i++)
    {
        calcs[i] = multipleMatrix(calcs[i - 1], calcs[i - 1]);
    }

    // for (int i = 0; i < binary_string.size(); i++)
    // {
    //     cout << "i:" << i << endl;
    //     printMatrix(calcs[i]);
    // }
    reverse(binary_string.begin(), binary_string.end());

    // cout << endl;
    // cout << binary_string << endl;

    vector<vector<int>> answer(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        answer[i][i] = 1;
    // printMatrix(answer);

    for (int i = 0; i < binary_string.size(); i++)
    {
        if (binary_string[i] == '1')
        {
            answer = multipleMatrix(answer, calcs[i]);
        }
    }
    // cout << "answer" << endl;
    printMatrix(answer);

    return 0;
}