#include <iostream>
using namespace std;

int d[11];

int main() {
	ios_base::sync_with_stdio;
	cin.tie(nullptr);
	
	d[0] = 1
;

	for (int i = 0; i <= 10; i++) {
		if (i - 1 >= 0) {
			d[i] += d[i - 1];
		}
		if (i - 2 >= 0) {
			d[i] += d[i - 2];
		}
		if (i - 3 >= 0) {
			d[i] += d[i - 3];
		}
	}

	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;
		cout << d[n] << '\n';
	}
	

	return 0;
}