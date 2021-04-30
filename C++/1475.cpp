#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string n;
int ans = 0;
int arr[10];
int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> n;

	for (int i = 0; i < n.size(); i++) {
		int num = n[i] - '0';
		if (num == 6 || num == 9) {
			arr[6]++;
			ans = max(ans, arr[6] / 2 + arr[6] % 2);
		}
		else {
			arr[num]++;
			ans = max(ans, arr[num]);
		}
	}

	
	cout << ans << endl;
	return 0;
}
