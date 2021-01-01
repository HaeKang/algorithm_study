#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	vector<int> v1, v2;

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		v1.push_back(x);		
	}

	int m;
	cin >> m;

	for (int j = 0; j < m; j++) {
		int x;
		cin >> x;
		v2.push_back(x);
	}

	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());

	vector<int> ans(n + m);

	int p1=0, p2=0, p3=0;

	while (p1 < n && p2 < m) {
		if (v1[p1] == v2[p2]) {
			ans[p3++] = v1[p1++];
			p2++;
		}
		else if (v1[p1] < v2[p2]) {
			p1++;
		}
		else {
			p2++;
		}
	}
	
	for (int k = 0; k < p3; k++) {
		cout << ans[k] << endl;
	}
	
	return 0;
}
