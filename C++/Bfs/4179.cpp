#include <iostream>
#include <string>
#include <queue>
#define MAX 1002

using namespace std;


int r, c;
char arr[MAX][MAX];

int fire[MAX][MAX];
int jh[MAX][MAX];
bool check_f[MAX][MAX];
bool check_j[MAX][MAX];

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };


int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	queue<pair<int, int>> qf;
	queue<pair<int, int>> qj;

	cin >> r >> c;

	for (int i = 0; i < r; i++) {
		string str;
		cin >> str;
		for (int j = 0; j < c; j++) {
			arr[i][j] = str[j];
			if (str[j] == 'F') {
				qf.push(make_pair(i, j));
				check_f[i][j] = true;
				fire[i][j] = 0;
			}
			if (str[j] == 'J') {
				qj.push(make_pair(i, j));
				check_j[i][j] = true;
				jh[i][j] = 0;
			}
		}
	}
	
	// fire bfs
	while (!qf.empty()) {
		int now_r = qf.front().first;
		int now_c = qf.front().second;
		qf.pop();

		for (int i = 0; i < 4; i++) {
			int nr = now_r + dx[i];
			int nc = now_c + dy[i];

			if (nr < 0 || nr >= r || nc < 0 || nc >= c) {
				continue;
			}

			if (check_f[nr][nc] || arr[nr][nc] == '#') {
				continue;
			}

			qf.push(make_pair(nr, nc));
			fire[nr][nc] = fire[now_r][now_c] + 1;
			check_f[nr][nc] = true;

		}
	}

	// 지훈
	while (!qj.empty()) {
		int now_r = qj.front().first;
		int now_c = qj.front().second;
		qj.pop();

		for (int i = 0; i < 4; i++) {
			int nr = now_r + dx[i];
			int nc = now_c + dy[i];

			if (check_j[nr][nc] || arr[nr][nc] == '#') {
				continue;
			}

			if (check_f[nr][nc] && fire[nr][nc] <= jh[now_r][now_c] + 1) {
				continue;
			}

			if (nr < 0 || nr >= r || nc < 0 || nc >= c) {
				cout << jh[now_r][now_c] + 1;
				return 0;
			}


			qj.push(make_pair(nr, nc));
			jh[nr][nc] = jh[now_r][now_c] + 1;
			check_j[nr][nc] = true;

		}

	}


	cout << "IMPOSSIBLE";
	return 0;
}
