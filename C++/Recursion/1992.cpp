#include <iostream>
#include <queue>
#include <string>
using namespace std;

/*
8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111
*/

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

int arr[66][66];	// [y][x] [row][col]
int n;
queue<int> q;

bool check(int x, int y, int size) {
	int end_x = x + size;
	int end_y = y + size;

	int cur = arr[y][x];
	
	for (int i = y; i < end_y; i++) {
		for (int j = x; j < end_x; j++) {
			if (cur != arr[i][j]) {
				return false;
			}
		}
	}

	return true;
}

void tree(int x, int y, int size) {
	bool state = check(x, y, size);
	if (state) {
		cout << arr[y][x];
		return;
	}
	else {
		cout << "(";
		int next_size = size / 2;
		tree(x, y, next_size);
		tree(x + next_size, y, next_size);
		tree(x, y + next_size, next_size);
		tree(x + next_size, y + next_size, next_size);
		cout << ")";
		return;
	}
}

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> n;
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < s.size(); j++) {
			arr[i][j] = s[j] - '0';
		}
	}

	tree(0, 0, n);

	return 0;
}
