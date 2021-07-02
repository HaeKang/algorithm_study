#include <iostream>
#include <vector>
#include <string>
using namespace std;

int n, arr[130][130];	// [y][x]
int blue, white;

bool check(int x, int y, int size) {
	int end_x = x + size;
	int end_y = y + size;

	int f = arr[y][x];

	for (int i = y; i < end_y; i++) {
		for (int j = x; j < end_x; j++) {
			if (arr[i][j] != f) {
				return false;
			}
		}
	}
	
	return true;
}

void paper(int x, int y, int size) {
	if (check(x, y, size)) {
		if (arr[y][x] == 0) {
			white++;
		}
		else {
			blue++;
		}
	}
	else {
		paper(x, y, size / 2);
		paper(x + size/2, y, size / 2);
		paper(x, y + size/2, size / 2);
		paper(x + size/2, y + size/2, size / 2);
	}
}

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	paper(0, 0, n);

	cout << white << '\n' << blue << '\n';
	return 0;
}
