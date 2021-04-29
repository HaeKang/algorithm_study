#include <iostream>
#include <string>
using namespace std;

int n, k, s, y;
int arr[7][2];
int ans;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> s >> y;
		arr[y][s]++;
	}
	
	for (int i = 1; i < 7; i++) {
		for (int j = 0; j < 2; j++) {
			int s = arr[i][j];
			if (s > 0) {
				if (s / k > 0) {
					ans += (s / k);
				}
				if (s % k != 0) {
					ans++;
				}
			}
		}
	}

	cout << ans << endl;
	return 0;
}
