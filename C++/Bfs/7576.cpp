#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int arr[1002][1002];	// [row][col]
int dist[1002][1002];
bool check[1002][1002];
int n, m, ans, no_tomato;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n;	// x, y
	
	queue<pair<int,int>> q;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 0) {
				no_tomato++;
			}
			if (arr[i][j] == 1) {
				q.push(make_pair(i, j));
				check[i][j] = true;
			}
		}
	}

	if (no_tomato == 0) {
		cout << "0\n";
		return 0;
	}

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
				if (!check[ny][nx] && arr[ny][nx] == 0) {
					check[ny][nx] = true;
					q.push(make_pair(ny, nx));
					dist[ny][nx] = dist[y][x] + 1;
					no_tomato--;
				}
			}

		}
	}

	if (no_tomato > 0) {
		cout << "-1\n";
		return 0;
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			ans = max(ans, dist[i][j]);
		}
	}

	cout << ans << '\n';
	return 0;
}
