#include <stdio.h>
#include <cstring>
#include <algorithm>

#define MAX 102
#define INF 987654321

using namespace std;

int v[MAX][MAX];

int n, m;

void kevin() {
	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (i == j) {
					continue;
				}
				else if (v[i][k] != 0 && v[k][j] != 0) {
					if (v[i][j] == 0) {
						v[i][j] = v[i][k] + v[k][j];
					}
					else {
						v[i][j] = min(v[i][j], v[i][k] + v[k][j]);
					}
				}

			}
		}
	}
}

int main() {
	scanf("%d %d", &n, &m);
	memset(v, 0, sizeof(v));
	for (int i = 0; i < m; i++) {
		int x, y;
		scanf("%d %d", &x, &y);
		v[x][y] = 1;
		v[y][x] = 1;
	}

	kevin();

	int result = INF;
	int person;

	for (int i = 1; i <= n; i++) {
		int sum = 0;
		for (int j = 1; j <= n; j++) {
			sum += v[i][j];
		}

		if (result > sum) {
			result = sum;
			person = i;
		}
	}

	printf("%d", person);
	return 0;

}
