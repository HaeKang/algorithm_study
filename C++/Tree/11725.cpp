#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>

using namespace std;
const int MAX = 100111;

vector<int> a[MAX];
int parent[MAX];
bool check[MAX];
int depth[MAX];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;	// node 개수
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int u, v;	// u : 부모 , v : 본인
		cin >> u >> v;
		a[u].push_back(v);
		a[v].push_back(u);
	}

	depth[1] = 0;	// 부모의 depth는 0
	check[1] = true;	// 부모 방문
	queue<int> q;
	q.push(1);
	parent[1] = 0;

	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			if (!check[y]) {
				depth[y] = depth[x] + 1;
				check[y] = true;
				parent[y] = x;
				q.push(y);
			}
		}
	}

	for (int i = 2; i <= n; i++) {
		cout << parent[i] << '\n';
	}

	return 0;
}