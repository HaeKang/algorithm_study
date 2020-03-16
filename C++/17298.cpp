#include <iostream>
#include <string>
#include <stack>

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
	bool tag = false;	// 현재 tag로 하는지
	stack<char> s;

	for (int i = 0; i < str.length(); i++) {

		if (str[i] == '<') {
			print(s);
			tag = true;
			cout << str[i];
		}
		else if(str[i] == '>'){
			tag = false;
			cout << str[i];
		}
		else if (tag) {
			cout << str[i];
		}
		else {
			if (str[i] == ' ') {
				print(s);
				cout << str[i];
			}
			else {
				s.push(str[i]);
			}
		}
	}
	print(s);
	cout << '\n';
	return 0;
}