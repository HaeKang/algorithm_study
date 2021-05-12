#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, k;
int cnt;
vector<int> v;

int main() {
	
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		int num;
		scanf("%d", &num);
		v.push_back(num);
	}
	
	for (int i = n - 1; i >= 0; i--) {
		if (k / v[i] > 0) {
			cnt += (k / v[i]);
			k -= v[i] * (k / v[i]);
		}
	}

	printf("%d", cnt);
	return 0;
}
