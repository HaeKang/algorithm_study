#include <iostream>
#include <algorithm>
using namespace std;

long long a[100001][2];
long long d[100001][3];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	cin >> t;
	
	while (t--) {
		int n;
		cin >> n;

		for (int i = 1; i <= n; i++) {
			cin >> a[i][0];
		}

		for (int i = 1; i <= n; i++) {
			cin >> a[i][1];
		}

		d[0][0] = 0;
		d[0][1] = 0;
		d[0][2] = 0;

		for (int i = 1; i <= n; i++) {
			d[i][0] = max(d[i - 1][0], max(d[i - 1][1], d[i - 1][2]));
			d[i][1] = max(d[i - 1][0], d[i - 1][2]) + a[i][0];
			d[i][2] = max(d[i - 1][0], d[i - 1][1]) + a[i][1];
		}

		long long ans = 0;
		for (int i = 1; i <= n; i++) {
			ans = max(max(ans, d[i][0]), max(d[i][1], d[i][2]));
		}

		cout << ans << '\n';
	}
	return 0;
}