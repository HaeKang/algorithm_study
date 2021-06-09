#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, m;
vector<int> e[22];
bool check[22];
int dis[22];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int n1, n2;
		cin >> n1 >> n2;
		e[n1].push_back(n2);
	}

	queue<int> q;
	q.push(1);
	check[1] = true;

	while (!q.empty()) {
		int node = q.front();
		q.pop();

		for (int i = 0; i < e[node].size(); i++) {
			int next_node = e[node][i];
			if (!check[next_node]) {
				q.push(next_node);
				check[next_node] = true;
				dis[next_node] = dis[node] + 1;
			}
		}

	}

	for (int i = 2; i <= n; i++) {
		cout << i << " : " << dis[i] << endl;
	}

	return 0;
}
