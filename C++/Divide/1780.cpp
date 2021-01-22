#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define MAX 2188

using namespace std;

int n;
int arr[MAX][MAX];
int ans[3];	// -1,0,1

bool check(int r, int c, int n) {
	for (int i = r; i < r+n; i++) {
		for (int j = c; j < c+n; j++) {
			if (arr[r][c] != arr[i][j]) {
				return false;
			}
		}
	}
	return true;
}

// 3으로 나누기
void divide(int r, int c, int n) {
	if (check(r, c, n)) {
		int num = arr[r][c];
		ans[num + 1]++;
		return;
	}

	int size = n / 3;

	for (int i = 0; i <3; i++) {
		for (int j = 0; j < 3; j++) {
			divide(r+i*size, c+j*size, size);
		}
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	memset(ans, 0, sizeof(ans));
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}
	
	divide(0, 0, n);
	
	for (int i = 0; i < 3; i++) {
		cout << ans[i] << endl;
	}

	return 0;
}
