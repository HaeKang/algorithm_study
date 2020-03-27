#include <iostream>
#include <queue>
#include <deque>

using namespace std;

bool c[1000000];
int d[1000000];
int MAX = 1000000;

int main() {
	int n, m;
	cin >> n >> m;
	
	c[n] = true;
	d[n] = 0;

	queue<int> q;
	queue<int> next_q;

	q.push(n);
	
	while (!q.empty()) {
		int now = q.front();
		q.pop();

		if (now * 2 < MAX) {
			if (c[now * 2] == false) {
				q.push(now * 2);
				c[now * 2] = true;
				d[now * 2] = d[now];
			}
		}

		if (now - 1 >= 0) {
			if (c[now - 1] == false) {
				next_q.push(now - 1);
				c[now - 1] = true;
				d[now - 1] = d[now] + 1;
			}
		}

		if (now + 1 < MAX) {
			if (c[now + 1] == false) {
				next_q.push(now + 1);
				c[now + 1] = true;
				d[now + 1] = d[now] + 1;
			}
		}

		// 현재큐 바꿔줌
		if (q.empty()) {
			q = next_q;
			next_q = queue<int>();
		}

	}

	cout << d[m] << '\n';
	return 0;

}
