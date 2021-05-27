#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[6] = { 0,0,1,-1,0,0 };
int dy[6] = { 1,-1,0,0,0,0 };
int dz[6] = { 0,0,0,0,1,-1 };
int arr[102][102][102];	// [row][col][h]
int dist[102][102][102];
bool check[102][102][102];
int n, m, h, ans, no_tomato;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n >> h;	// x, y, h
	
	queue<pair<int,pair<int,int>>> q;

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				cin >> arr[j][k][i];	// y x z
				if (arr[j][k][i] == 0) {
					no_tomato++;
				}
				if (arr[j][k][i] == 1) {
					q.push(make_pair(j, make_pair(k, i)));	// y, x, z
					check[j][k][i] = true;
				}
			}
		}
	}
	

	if (no_tomato == 0) {
		cout << "0\n";
		return 0;
	}

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second.first;
		int z = q.front().second.second;
		q.pop();

		for (int i = 0; i < 6; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			int nz = z + dz[i];

			if (nx >= 0 && nx < m && ny >= 0 && ny < n && nz >= 0 && nz < h) {
				if (arr[ny][nx][nz] == 0 && !check[ny][nx][nz]) {
					q.push(make_pair(ny, make_pair(nx, nz)));
					arr[ny][nx][nz] = 1;
					check[ny][nx][nz] = true;
					dist[ny][nx][nz] = dist[y][x][z] + 1;
					no_tomato--;
				}
			}

		}
		
	}

	if (no_tomato > 0) {
		cout << "-1\n";
		return 0;
	}

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < m; k++) {
				ans = max(ans, dist[j][k][i]);
			}
		}
	}

	cout << ans << '\n';
	return 0;
}
