#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);	// 각 값

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	vector<int> d(n);	// 최대값

	for (int i = 0; i < n; i++) {
		d[i] = a[i];
		for (int j = 0; j < i; j++) {
			if (a[j] < a[i] && d[j] + a[i] > d[i]) {
				d[i] = d[j] + a[i];
			}
		}
	}

	int ans = *max_element(d.begin(), d.end());
	cout << ans << '\n';
	return 0;
}