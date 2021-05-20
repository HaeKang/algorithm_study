#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
vector<int> v;
int arr[4];	// + - * /
int ans_min = 1000000001;
int ans_max = -1000000001;

void dfs(int idx, int result, int a1, int a2, int a3, int a4) {

	if (idx == n) {
		ans_min = min(ans_min, result);
		ans_max = max(ans_max, result);
		return;
	} 

	if (a1 > 0) {
		dfs(idx + 1, result + v[idx], a1 - 1, a2, a3, a4);
	}

	if (a2 > 0) {
		dfs(idx + 1, result - v[idx], a1, a2 - 1, a3, a4);
	}

	if (a3 > 0) {
		dfs(idx + 1, result * v[idx], a1, a2, a3 - 1, a4);
	}
	
	if (a4 > 0) {
		dfs(idx + 1, result / v[idx], a1, a2, a3, a4 - 1);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		int n2;
		cin >> n2;
		v.push_back(n2);
	}
	
	for (int i = 0; i < 4; i++) {
		cin >> arr[i];
	}

	dfs(1, v[0], arr[0], arr[1], arr[2], arr[3]);

	cout << ans_max << '\n' << ans_min << '\n';
	return 0;
}
