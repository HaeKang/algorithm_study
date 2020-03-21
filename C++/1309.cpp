#include <iostream>
#include <algorithm>
using namespace std;

int mod = 9901;
int d[100001][3];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	d[0][0] = 1;

	for (int i = 1; i <= n; i++) {
		d[i][0] = d[i - 1][0] + d[i - 1][1] + d[i - 1][2];
		d[i][1] = d[i - 1][0] + d[i - 1][2];
		d[i][2] = d[i - 1][0] + d[i - 1][1];
		for (int j = 0; j < 3; j++) {
			d[i][j] %= mod;
		}
	}

	cout << (d[n][0] + d[n][1] + d[n][2]) % mod << '\n';

	return 0;
}