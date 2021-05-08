#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	stack<char> s;
	string str;
	int ans = 0;

	cin >> str;

	for (int i = 0; i < str.size(); i++) {
		char c = str[i];

		if (c == ')') {
			if (str[i-1] == '(') {
				// 레이저
				s.pop();
				ans += s.size();
			}
			else {
				s.pop();
				ans++;
			}
		}
		else {
			s.push(c);
		}

	}
	
	cout << ans << endl;
	return 0;
}
