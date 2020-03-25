#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> a[3000];
int check[3000]; // 0: not visited, 1: visited, 2: cycle
int dist[3000];


int go(int x, int p) {

	// -2: found cycle and not included
	// -1: not found cycle
	// 0~n-1: found cycle and start index

	if (check[x] == 1) {
		return x;	// cycle의 시작 index return
	}

	check[x] = 1;

	for (int y : a[x]) {
		if (y == p) continue;

		int res = go(y, x);

		if (res == -2) return -2;

		if (res >= 0) {

			check[x] = 2;
			if (x == res) return -2;	// 현재 정점이 res(cycle시작점)이랑 같으면
			else return res;

		}
	}
	return -1;
}
int main() {

	int n;
	cin >> n;

	for (int i = 0; i<n; i++) {
		int u, v;
		cin >> u >> v;

		u -= 1; 
		v -= 1;

		a[u].push_back(v);
		a[v].push_back(u);

	}

	go(0, -1);
	queue<int> q;

	for (int i = 0; i<n; i++) {
		if (check[i] == 2) {	// 시작점
			dist[i] = 0;	//시작점의 거리는 0
			q.push(i);	
		}
		else {
			dist[i] = -1;	// 아직 못구함을 의미
		}
	}


	while (!q.empty()) {
		int x = q.front(); q.pop();
		for (int y : a[x]) {
			if (dist[y] == -1) {
				q.push(y);	// 방문 하고 거리 업데이트
				dist[y] = dist[x] + 1;
			}
		}
	}
	for (int i = 0; i<n; i++) {
		cout << dist[i] << ' ';
	}
	cout << '\n';
	return 0;
}