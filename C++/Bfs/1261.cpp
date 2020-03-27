#include <iostream>
#include <queue>
#include <string>

using namespace std;

int n, m;
int d[555][555];
int a[555][555];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> m >> n;


	for (int i = 0; i<n; i++) {
		char str[555];
		cin >> str;
		for (int j = 0; j<m; j++) {
			a[i][j] = str[j] -'0';
			d[i][j] = -1;
		}
	}

	queue<pair<int, int>> q;
	queue<pair<int, int>> next_queue;

	q.push(make_pair(0, 0));
	d[0][0] = 0;

	while (!q.empty()) {

		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int k = 0; k<4; k++) {

			int nx = x + dx[k];
			int ny = y + dy[k];

			if (0 <= nx && nx < n && 0 <= ny && ny < m) {

				if (d[nx][ny] == -1) {

					if (a[nx][ny] == 0) {

						d[nx][ny] = d[x][y];
						q.push(make_pair(nx, ny));

					}
					else {

						d[nx][ny] = d[x][y] + 1;
						next_queue.push(make_pair(nx, ny));

					}
				}
			}
		}

		if (q.empty()) {

			q = next_queue;
			next_queue = queue<pair<int, int>>();

		}
	}

	cout << d[n - 1][m - 1] << '\n';
	return 0;
}