#include <iostream>
#include <vector>
using namespace std;

typedef int Key;

struct Element {
    int id;
    Key key;
};

vector<Element> H;
vector<int> xmap;
int n;

inline int LeftChild(int i) { return 2 * i; }
inline int RightChild(int i) { return 2 * i + 1; }
inline int Parent(int i) { return i / 2; }

void SwapHeap(int i, int j)
{
    swap(H[i], H[j]);
    swap(xmap[H[i].id], xmap[H[j].id]);
}

void UpHeap(int i)
{
    while(i > 1 && H[Parent(i)].key > H[i].key) {
        SwapHeap(i, Parent(i));
        i = Parent(i);
    }
}

void DecreaseKey(int id, Key key)
{
    int i = xmap[id];
    H[i].key = key;
    UpHeap(i);
}

void Insert(int id, int key)
{
    ++n;
    H[n].id = id;
    H[n].key = key;
    xmap[id] = n;
    UpHeap(n);
}

void Heapify(int i)
{
    while(true) {
        int left = LeftChild(i), right = RightChild(i);
        int smallest = i;

        if(left <= n && H[left].key < H[smallest].key) smallest = left;
        if(right <= n && H[right].key < H[smallest].key) smallest = right;

        if(smallest == i) break;
        SwapHeap(i, smallest);
        i = smallest;
    }
}

int DeleteMin()
{
    int min_id = H[1].id;
    SwapHeap(1, n);
    --n;
    Heapify(1);
    return min_id;
}

void CreateHeap()
{
    for(int i = n/2; i >= 1; --i)
        Heapify(i);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while(t--)
    {
        int num_elements, width;
        cin >> num_elements >> width;

        // 각 테스트케이스마다 초기화
        H.assign(width + 1, Element());
        xmap.assign(num_elements + 1, 0);

        n = width;

        for(int i = 1; i <= width; ++i)
        {
            int val;
            cin >> val;
            H[i].id = i;
            H[i].key = val;
            xmap[i] = i;
        }

        CreateHeap();

        vector<int> ans;
        ans.reserve(max(0, num_elements - width + 1));

        for(int i = width + 1, delete_id = 1; i <= num_elements; ++i, ++delete_id)
        {
            ans.push_back(H[1].key);

            if(H[1].id != delete_id)
                DecreaseKey(delete_id, 0);

            DeleteMin();

            int val;
            cin >> val;
            Insert(i, val);
        }

        ans.push_back(H[1].key);

        long long sum = 0;
        for(int v : ans)
        {
            sum += v;
            sum %= 100000007;
        }

        cout << sum << endl;   // 테스트 케이스별 출력 1줄
    }

    return 0;
}
