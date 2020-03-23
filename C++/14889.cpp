#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int s[20][20];

int go(int index, vector<int> &fi, vector<int> &se) {
	if (index == n) {
		if (fi.size() != n / 2) {
			return -1;
		}
		if (se.size() != n / 2) {
			return -1;
		}

		int t1 = 0;	// ´É·ÂÄ¡
		int t2 = 0;

		for (int i = 0; i < n / 2; i++) {
			for (int j = 0; j < n / 2; j++) {
				if (i == j) {
					continue;
				}
				t1 += s[fi[i]][fi[j]];
				t2 += s[se[i]][se[j]];
			}
		}

		int diff = t1 - t2;
		if (diff < 0) {
			diff = -diff;
		}
		return diff;
	}
	
	int ans = -1;
	
	// 1¹øÆÀ
	fi.push_back(index);
	int t1 = go(index + 1, fi, se);	
	if (ans == -1 || (t1 != -1 && ans > t1)) {
		ans = t1;
	}
	fi.pop_back();

	// 2¹øÆÀ
	se.push_back(index);
	int t2 = go(index + 1, fi, se);
	if (ans == -1 || (t2 != -1 && ans > t2)) {
		ans = t2;
	}

	se.pop_back();
	return ans;

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n;
	for (int i = 0; i<n; i++) {
		for (int j = 0; j<n; j++) {
			cin >> s[i][j];
		}
	}
	vector<int> first, second;
	cout << go(0, first, second) << '\n';

	return 0;
}