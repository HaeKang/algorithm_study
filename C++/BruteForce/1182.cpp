#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, s, ans;
int arr[22];

void fun(int idx, int sum) {
	if (idx >= n) {
		return;
	}

	if (sum+arr[idx] == s) {
		ans++;
	}

	fun(idx + 1, sum + arr[idx]);
	fun(idx + 1, sum);

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> s;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	fun(0, 0);
	cout << ans << '\n';
	return 0;
}
