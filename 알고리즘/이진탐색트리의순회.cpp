#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int val;
    Node *left, *right;
    Node(int v) : val(v), left(NULL), right(NULL) {}
};

Node *buildFromPre(const vector<int> &a, int l, int r)
{
    if (l > r)
        return NULL;
    Node *root = new Node(a[l]);
    int mid = l + 1;

    while (mid <= r && a[mid] < a[l])
        mid++;

    root->left = buildFromPre(a, l + 1, mid - 1);
    root->right = buildFromPre(a, mid, r);

    return root;
}

Node *buildFromPost(const vector<int> &a, int l, int r)
{
    if (l > r)
        return NULL;
    Node *root = new Node(a[r]);
    int mid = r - 1;

    while (mid >= l && a[mid] > a[r])
        mid--;

    root->left = buildFromPost(a, l, mid);
    root->right = buildFromPost(a, mid + 1, r - 1);

    return root;
}

void preorder(Node *root, vector<int> &out)
{
    if (!root)
        return;
    out.push_back(root->val);
    preorder(root->left, out);
    preorder(root->right, out);
}

void postorder(Node *root, vector<int> &out)
{
    if (!root)
        return;
    postorder(root->left, out);
    postorder(root->right, out);
    out.push_back(root->val);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        int N, type;
        cin >> N >> type;

        vector<int> a(N);
        for (int i = 0; i < N; i++)
            cin >> a[i];

        Node *root = NULL;
        vector<int> result;

        if (type == 1)
        {
            root = buildFromPre(a, 0, N - 1);
            postorder(root, result);
        }
        else
        {
            root = buildFromPost(a, 0, N - 1);
            preorder(root, result);
        }

        for (int i = 0; i < N; i++)
        {
            cout << result[i];
            if (i + 1 < N)
                cout << " ";
        }
        cout << endl;
    }
}
