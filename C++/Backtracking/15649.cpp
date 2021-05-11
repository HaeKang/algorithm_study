#include <iostream>

using namespace std;

int n, m;
int arr[10];
bool check[10];

void back(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			printf("%d ", arr[i]);
		}
		printf("\n");
		return;
	}

	for (int i = 1; i <= n; i++) {
		if (!check[i]) {
			arr[k] = i;
			check[i] = true;
			back(k + 1);
			check[i] = false;
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);
	back(0);
	return 0;
}
