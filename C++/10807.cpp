#include <iostream>
#include <string>
using namespace std;

int n, f, ans = 0;
int arr[101];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);


	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> f;

	for (int i = 0; i < n; i++) {
		if (arr[i] == f) {
			ans++;
		}
	}

	cout << ans << endl;
	return 0;
}
