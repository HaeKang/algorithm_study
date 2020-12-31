#include <iostream>

using namespace std;

void insertion_sort(int list[], int n) {
	int i, j;
	for (i = 1; i < n; i++) {
		int tmp = list[i];
		for (j = i - 1; j >= 0; j--) {
			if (list[j] > tmp) {
				list[j + 1] = list[j];
			}
		}
		list[j + 1] = tmp;	// j가 -1이 되서 끝나므로 j+1
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
	
	insertion_sort(list, n);

	return 0;
}
