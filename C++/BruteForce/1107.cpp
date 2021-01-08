#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

int n, m, ans;
bool err[11];



int length(int n) {
	if (n == 0) {
		if (err[0]) {
			return 0;
		}
		else {
			return 1;
		}
	}
	else {
		int len = 0;
		while (n > 0) {
			if (err[n % 10]) {
				return 0;
			}
			else {
				n /= 10;
				len += 1;
			}
		}
		return len;
	}
}

int main()
{
	scanf("%d", &n);
	scanf("%d", &m);

	memset(err, false, sizeof(err));

	for (int i = 0; i < m; i++) {
		int tmp;
		scanf("%d", &tmp);
		err[tmp] = true;
	}

	ans = abs(n - 100);

	for (int i = 0; i <= 1000000; i++) {
		int c = i;
		int len = length(c);
		if (len > 0) {
			int p = abs(c - n);
			if (ans > p + len) {
				ans = p + len;
			}
		}
	}

	printf("%d\n", ans);
	return 0;
}
