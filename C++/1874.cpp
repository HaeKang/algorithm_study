#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string ans;
	int n;
	stack<int> s;

	cin >> n;

	int m = 0;	// ���ÿ� �� ������ ��

	while (n--) {
		int x;	// ���� ��
		cin >> x;
		if (x > m) {
			while (x > m) {
				s.push(++m);	// ���̿� �ִ� �� �־���
				ans += '+';
			}
			s.pop();
			ans += '-';
		}
		else {
			bool found = false;
			if (!s.empty()) {
				int top = s.top();
				s.pop();
				ans += '-';
				if (x == top) {
					found = true;
				}
			}

			if (!found) {
				cout << "NO" << '\n';
				return 0;
			}
		}
	}

	for (auto x : ans) {
		cout << x << '\n';
	}

	return 0;
}