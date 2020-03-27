#include <iostream>
#include <tuple>
#include <queue>
#include <cstring>

using namespace std;
int d[1001][1001];	// -1 : 방문X

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	memset(d, -1, sizeof(d));

	queue<pair<int, int>> q;
	q.push(make_pair(1, 0));	// 화면 이모티콘 개수, 클립보드개수
	d[1][0] = 0;


	while (!q.empty()) {

		int s, c;
		tie(s, c) = q.front();
		q.pop();

		// 복사
		if (d[s][s] == -1) {

			d[s][s] = d[s][c] + 1;
			q.push(make_pair(s, s));

		}

		// 붙여넣기
		if (s + c <= n && d[s + c][c] == -1) {

			d[s + c][c] = d[s][c] + 1;
			q.push(make_pair(s + c, c));

		}

		// 삭제
		if (s - 1 >= 0 && d[s - 1][c] == -1) {

			d[s - 1][c] = d[s][c] + 1;
			q.push(make_pair(s - 1, c));

		}
	}

	int ans = -1;
	for (int i = 0; i <= n; i++) {
		if (d[n][i] != -1) {
			if (ans == -1 || ans > d[n][i]) {
				ans = d[n][i];
			}
		}
	}

	cout << ans << '\n';
	return 0;
}