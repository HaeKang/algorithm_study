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

	int m = 0;	// 스택에 들어간 마지막 수

	while (n--) {
		int x;	// 현재 수
		cin >> x;
		if (x > m) {
			while (x > m) {
				s.push(++m);	// 사이에 있는 수 넣어줌
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