#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int k;
int arr[52];
int ans[52];

void lotto(int idx, int len) {
	if (len > 6 ){
		for (int i = 1; i < 7; i++) {
			cout << ans[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = idx; i < k; i++) {
		ans[len] = arr[i];
		lotto(i+1, len + 1);
	}
	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	while (true) {
		cin >> k;
		if (k == 0) {
			break;
		}

		for (int i = 0; i < k; i++) {
			cin >> arr[i];
		}

		lotto(0,1);
		cout << '\n';
	}

	return 0;
}
