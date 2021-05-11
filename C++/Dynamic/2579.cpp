#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[302];
int sum[302];

int main() {

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}

	sum[0] = arr[0];
	sum[1] = arr[0] + arr[1];
	sum[2] = max(arr[0] + arr[2], arr[1] + arr[2]);

	for (int i = 3; i < n; i++) {
		sum[i] = max(sum[i - 3] + arr[i - 1] + arr[i], sum[i - 2] + arr[i]);
	}

	printf("%d\n", sum[n - 1]);
	return 0;
}
