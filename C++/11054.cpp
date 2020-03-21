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
	vector<int> d_up(n);
	vector<int> d_down(n);

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for (int i = 0; i < n; i++) {
		d_up[i] = 1;
		for (int j = 0; j < i; j++) {
			if (a[j]<a[i] && d_up[j] + 1 > d_up[i]) {
				d_up[i] = d_up[j] + 1;
			}
		}
	}

	for (int i = n - 1; i >= 0; i--) {
		d_down[i] = 1;
		for (int j = i + 1; j < n; j++) {
			if (a[i] > a[j] && d_down[j] + 1 > d_down[i]) {
				d_down[i] = d_down[j] + 1;
			}
		}
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (ans < d_up[i] + d_down[i] - 1) {
			ans = d_up[i] + d_down[i] - 1;
		}
	}

	cout << ans << '\n';

	return 0;
}