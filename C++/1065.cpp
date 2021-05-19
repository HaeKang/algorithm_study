#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int n;
int cnt;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	
	if (n < 100) {
		cout << n << '\n';
		return 0;
	}
	

	for (int i = 100; i <= n; i++) {
		int h = i / 100;
		int t = (i - h * 100) / 10;
		int o = i % 10;

		if (h - t == t - o) {
			cnt++;
		}

	}

	cout << cnt + 99 << '\n';
	return 0;
}
