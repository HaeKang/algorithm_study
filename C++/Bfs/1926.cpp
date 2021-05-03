#include <iostream>
#include <vector>
#include <queue>
#define MAX 501

using namespace std;

int n, m;
int arr[MAX][MAX];
bool visit[MAX][MAX];

int cnt, max_area;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
		}
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (arr[i][j] == 1 && !visit[i][j]) {
				
				queue<pair<int, int>> q;
				int area = 0;

				q.push(make_pair(i, j));
				visit[i][j] = true;
				cnt++;

				while (!q.empty()) {
					area++;
					int x = q.front().first;
					int y = q.front().second;
					q.pop();

					for (int k = 0; k < 4; k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];

						if (0 <= nx && nx < MAX && 0 <= ny && ny < MAX) {
							if (arr[nx][ny] == 1 && !visit[nx][ny]) {
								visit[nx][ny] = true;
								q.push(make_pair(nx, ny));
							}
						}
					}

				}

				if (area > max_area) {
					max_area = area;
				}
			}
		}
	}
	
	cout << cnt << endl;
	cout << max_area << endl;
	return 0;
}
