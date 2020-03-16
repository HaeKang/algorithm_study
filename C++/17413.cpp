#include <iostream>
#include <stack>
#include <string>

using namespace std;

void print(stack<char> &s) {
	while (!s.empty()) {
		cout << s.top();
		s.pop();
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string str;
	getline(cin, str);
	bool tag = false;	
	stack<char> s;

	for (char ch : str) {
		if (ch == '<') {
			tag = true;
			print(s);
			cout << ch;

		}
		else if (ch == '>') {
			tag = false;
			cout << ch;
		}
		else if (tag) {
			cout << ch;
		}
		else {
			if (ch == ' ') {
				print(s);
				cout << ch;
			}
			else {
				s.push(ch);
			}
		}
	}

	print(s);
	cout << '\n';
	return 0;

}