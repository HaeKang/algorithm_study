#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int m, n, k, cnt;	// m : col(x), n : row(y)
int arr[102][102];	// [n][m] == [y][x]
bool check[102][102];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
vector<int> ans;

void dfs(int x, int y) {
	check[y][x] = true;

	cnt++;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
			continue;
		}

		if (arr[ny][nx] == 1 || check[ny][nx]) {
			continue;
		}

		dfs(nx, ny);

	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> m >> n >> k;
	for (int i = 0; i < k; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int j = y1; j < y2; j++) {
			for (int o = x1; o < x2; o++) {
				arr[j][o] = 1;
			}
		}
	}
	
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == 0 && !check[i][j]) {
				cnt = 0;
				dfs(j, i);
				ans.push_back(cnt);
			}
		}
	}

	sort(ans.begin(), ans.end());
	cout << ans.size() << '\n';
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << " ";
	}

	return 0;
}
