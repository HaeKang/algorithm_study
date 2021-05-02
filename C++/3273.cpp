#include <iostream>
#include <string>
#include <algorithm>
#define MAX 1000001

using namespace std;

int n, x, ans, num;
int arr[MAX];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> num;
		arr[num]++;
	}

	cin >> x;

	for (int i = 1; i < x; i++) {
		if (arr[i] > 0) {
			if (arr[abs(x - i)] == 1 && abs(x-i) != i) {
				ans++;
				arr[i] = 0;
			}
		}
	}


	cout << ans << endl;
	return 0;
}
