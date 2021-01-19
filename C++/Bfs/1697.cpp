#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>

#define MAX 100001

using namespace std;

int n, k;
bool visit[MAX];
int dis[MAX];

int bfs(int start, int end) {
	queue<int> q;
	q.push(start);
	visit[start] = true;

	while (!q.empty()) {
		int x = q.front();
		int distance = dis[x];
		q.pop();

		if (x == end) {
			return distance;
			break;
		}

		if (x - 1 >= 0 && !visit[x - 1]) {
			q.push(x - 1);
			visit[x - 1] = true;
			dis[x - 1] = distance + 1;
		}

		if (x + 1 < MAX && !visit[x + 1]) {
			q.push(x + 1);
			visit[x + 1] = true;
			dis[x + 1] = distance + 1;
		}

		if (x * 2 < MAX && !visit[x * 2]) {
			q.push(x * 2);
			visit[x * 2] = true;
			dis[x * 2] = distance + 1;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	memset(visit, false, sizeof(visit));
	memset(dis, 0, sizeof(dis));
	cin >> n >> k;
	cout << bfs(n, k) << endl;


	return 0;
}
