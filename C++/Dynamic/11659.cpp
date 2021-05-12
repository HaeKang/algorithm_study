#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
int arr[100002];
int dp[100002];

int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	dp[0] = arr[0];
	for (int i = 1; i < n; i++) {
		dp[i] = dp[i - 1] + arr[i];
	}


	for (int i = 0; i < m; i++) {
		int start, end, ans;
		scanf("%d %d", &start, &end);

		if (start == 1) {
			ans = dp[end-1];
		}
		else {
			ans = dp[end-1] - dp[start-1] + arr[start-1];
		}

		printf("%d\n", ans);
	}

	return 0;
}
