#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> a[100000];
bool check[100000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int n;
	cin >> n;

	for (int i = 0; i < n - 1; i++) {
		int u, v;
		cin >> u >> v;
		u -= 1;
		v -= 1;
		a[u].push_back(v);
		a[v].push_back(u);
	}

	vector<int> b(n);
	vector<int> order(n);

	for (int i = 0; i < n; i++) {
		cin >> b[i];
		b[i] -= 1;
		order[b[i]] = i;
	}

	for (int i = 0; i < n; i++) {
		sort(a[i].begin(), a[i].end(), [&](const int &u, const int &v) {
			return order[u] < order[v];
		});
	}

	vector<int> bfs_order;
	queue<int> q;
	q.push(0);
	check[0] = true;

	while (!q.empty()) {
		int x = q.front();
		q.pop();
		bfs_order.push_back(x);
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			if (check[y] == false) {
				check[y] = true;
				q.push(y);
			}
		}
	}

	if (bfs_order == b) {
		cout << 1 << '\n';
	}
	else {
		cout << 0 << '\n';
	}

	return 0;
}