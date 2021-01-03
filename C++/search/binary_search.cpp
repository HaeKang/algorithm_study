#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int n, m;

	scanf("%d %d", &n, &m);

	vector<int> v;
	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		v.push_back(tmp);
	}
	
	sort(v.begin(), v.end());

	int lp = 0;
	int rp = n - 1;

	while (lp <= rp) {
		int mid = (lp + rp) / 2;

		if (v[mid] == m) {
			printf("%d\n", mid + 1);
			return 0;
		}
		else if (v[mid] > m) {
			rp = mid - 1;
		}
		else {
			lp = mid + 1;
		}
	}


	return 0;
}
