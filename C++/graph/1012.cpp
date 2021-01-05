#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int arr[51][51] = { 0,  };
bool check[51][51];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };
int t, n, m, k;

void dfs(int x, int y) {

	check[x][y] = true;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
			continue;
		}

		if (arr[nx][ny] == 1 &&  !check[nx][ny]) {
			dfs(nx, ny);			
		}
	}

}

int main() {
	scanf("%d", &t);

	for (int tc = 0; tc < t; tc++) {
		scanf("%d %d %d", &n, &m, &k);

		memset(arr, 0, sizeof(arr));
		memset(check, false, sizeof(check));

		int ans = 0;

		for (int i = 0; i < k; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			arr[x][y] = 1;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (arr[i][j] == 1 && !check[i][j]) {
					dfs(i, j);
					ans++;
				}
			}
		}
		printf("%d\n", ans);
	}

	return 0;
}
