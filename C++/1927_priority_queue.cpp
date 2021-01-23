#include <iostream>
#include <stdio.h>
#include <queue>
#include <functional>

#define MAX 100001

using namespace std;

int n;
priority_queue<int, vector<int>, greater<int>> q;


int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x);
		if (x == 0) {
			if (!q.empty()) {
				printf("%d\n", q.top());
				q.pop();
			}
			else {
				printf("0\n");
			}
		}
		else {
			q.push(x);
		}
	}
	return 0;
}
