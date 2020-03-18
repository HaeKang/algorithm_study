#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio;
	cin.tie(nullptr);

	int n;
	cin >> n;
	vector<int> a(n + 1);
	vector<int> d(n + 1, -1);

	for (int i = 1; i <= n; i++) {
		cin >> a[i];
	}

	d[0] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			if (d[i] == -1 || d[i] > d[i - j] + a[j]) {
				d[i] = d[i - j] + a[j];
			}
		}
	}

	cout << d[n] << '\n';

	
	return 0;
}