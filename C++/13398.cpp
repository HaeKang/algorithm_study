#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	vector<int> a(n);
	vector<int> d(n);	// i번째에서 끝나는 연속합
	vector<int> dr(n);	// i번째부터 시작하는 연속합

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for (int i = 0; i < n; i++) {
		d[i] = a[i];
		if (i == 0) {
			continue;
		}

		if (d[i] < d[i - 1] + a[i]) {
			d[i] = d[i - 1] + a[i];
		}
	}

	for (int i = n - 1; i >= 0; i--) {
		dr[i] = a[i];
		if (i == n - 1) {
			continue;
		}
		if (dr[i] < dr[i + 1] + a[i]) {
			dr[i] = dr[i + 1] + a[i];
		}
	}
	int ans = d[0];
	for (int i = 1; i<n; i++) {
		if (ans < d[i]) {
			ans = d[i];
		}
	}
	for (int i = 1; i<n - 1; i++) {
		if (ans < d[i - 1] + dr[i + 1]) {
			ans = d[i - 1] + dr[i + 1];
		}
	}
	cout << ans << '\n';
	return 0;

}