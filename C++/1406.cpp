#include <iostream>
#include <cstring>
#include <stack>

using namespace std;
char str[600000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	stack<char> s_r, s_l;

	cin >> str;
	int str_len = strlen(str);
	for (int i = 0; i < str_len; i++) {
		s_l.push(str[i]);
	}

	int n;
	cin >> n;

	while (n--) {
		char msg;
		cin >> msg;

		if (msg == 'L') {
			if (!s_l.empty()) {
				s_r.push(s_l.top());
				s_l.pop();
			}
		} 
		else if (msg == 'D') {
			if (!s_r.empty()) {
				s_l.push(s_r.top());
				s_r.pop();
			}
		}
		else if (msg == 'B') {
			if (!s_l.empty()) {
				s_l.pop();
			}
		}
		else if (msg == 'P') {
			char c;
			cin >> c;
			s_l.push(c);
		}
	}

	while (!s_l.empty()) {
		s_r.push(s_l.top());
		s_l.pop();
	}

	while (!s_r.empty()) {
		printf("%c", s_r.top());
		s_r.pop();
	}

	printf("\n");
	return 0;

}