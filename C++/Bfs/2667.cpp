#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> ans;
int n, cnt;
int arr[27][27];
bool check[27][27];

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

void dfs(int x, int y) {
	check[y][x] = true;
	cnt++;

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
			continue;
		}

		if (check[ny][nx] || arr[ny][nx] == 0) {
			continue;
		}

		dfs(nx, ny);
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {	// y
		string str;
		cin >> str;
		for (int j = 0; j < str.size(); j++) {	//x
			arr[i][j] = str[j] - '0';
		}

	}


	for (int i = 0; i < n; i++) {	//y
		for (int j = 0; j < n; j++) {	//x
			if (!check[i][j] && arr[i][j] == 1) {
				cnt = 0;
				dfs(j, i);
				ans.push_back(cnt);
			}
		}
	}


	sort(ans.begin(), ans.end());
	cout << ans.size() << '\n';
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << '\n';
	}

	return 0;
}
