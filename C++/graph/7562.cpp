#include <iostream>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring> // memset
using namespace std;

int d[300][300];
int dx[] = { -2,-1,1,2,2,1,-1,-2 };
int dy[] = { 1,2,2,1,-1,-2,-2,-1 };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;

		int sx, sy;
		cin >> sx >> sy;

		int ex, ey;
		cin >> ex >> ey;

		memset(d, -1, sizeof(d));

		queue<pair<int, int>> q;
		q.push(make_pair(sx, sy));
		d[sx][sy] = 0;

		while (!q.empty()) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			for (int k = 0; k < 8; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];

				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					if (d[nx][ny] == -1) {
						d[nx][ny] = d[x][y] + 1;
						q.push(make_pair(nx, ny));
					}
				}
			}
		}

		cout << d[ex][ey] << '\n';

	}

	return 0;
}