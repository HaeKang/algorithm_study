#include <iostream>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring> // memset
using namespace std;

int n, m;
int a[100][100];
bool check[100][100];
int dist[100][100];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> m;
	

	for (int i = 0; i<n; i++) {
		string temp;
		cin >> temp;

		for (int j = 0; j<m; j++) {
			a[i][j] = temp[j] - '0';
		}
	}

	memset(check, false, sizeof(check));
	queue<pair<int, int>> q;
	q.push(make_pair(0, 0));


	check[0][0] = true;
	dist[0][0] = 1;

	while (!q.empty()) {

		int x = q.front().first;
		int y = q.front().second;
		q.pop();

		for (int k = 0; k<4; k++) {

			int nx = x + dx[k];
			int ny = y + dy[k];

			if (0 <= nx && nx < n && 0 <= ny && ny < m) {

				if (check[nx][ny] == false && a[nx][ny] == 1) {

					q.push(make_pair(nx, ny));
					dist[nx][ny] = dist[x][y] + 1;
					check[nx][ny] = true;

				}
			}
		}
	}

	cout << dist[n - 1][m - 1] << '\n';
	return 0;
}