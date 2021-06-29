#include <iostream>
#include <vector>
#include <string>
using namespace std;


int n, edge, ans;
vector<int> v[102];
bool check[102];

void dfs(int node) {
	check[node] = true;
	ans++;

	for (int i = 0; i < v[node].size(); i++) {
		if (!check[v[node][i]]) {
			dfs(v[node][i]);
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> n;
	cin >> edge;
	for (int i = 0; i < edge; i++) {
		int n1, n2;
		cin >> n1 >> n2;
		v[n1].push_back(n2);
		v[n2].push_back(n1);
	}

	dfs(1);
	cout << ans-1 << endl;
	return 0;
}
