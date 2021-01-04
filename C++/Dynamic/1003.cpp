#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int dp[41] = { 0,1 };

int main() {
	
	int n;
	scanf("%d", &n);

	for (int j = 2; j <= 40; j++) {
		dp[j] = dp[j - 1] + dp[j - 2];
	}


	for (int i = 0; i < n; i++) {
		int tmp;
		scanf("%d", &tmp);
		
		if (tmp == 0) {
			printf("1 0\n");
		}
		else {
			int zero = dp[tmp - 1];
			int one = dp[tmp];

			printf("%d %d\n", zero, one);
		}
	}



	return 0;
}
