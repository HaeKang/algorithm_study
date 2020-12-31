#include <iostream>

using namespace std;

void bubble_sort(int list[], int n) {
	for (int i = 0; i < n-1; i++) {
		for (int j = 0; j < n - i; j++) {
			if (list[j] > list[j + 1]) {
				int tmp = list[j];
				list[j] = list[j + 1];
				list[j + 1] = tmp;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	int list[101];
	for (int i = 0; i < n; i++) {
		cin >> list[i];
	}
	
	bubble_sort(list, n);

	return 0;
}
