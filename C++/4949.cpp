#include <iostream>
#include <string>
#include <stack>

using namespace std;



int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	while (true) {

		string str;
		stack<char> s;
		bool check = true;

		getline(cin, str);
		
		if (str == ".") {
			break;
		}
		else {
			for (int i = 0; i < str.size(); i++) {
				if (str[i] == '(' || str[i] == '[') {
					s.push(str[i]);
				}
				else if (str[i] == ')') {
					if (s.empty() || s.top() != '(') {
						check = false;
						break;
					}
					else {
						s.pop();
					}
				}
				else if (str[i] == ']') {
					if (s.empty() || s.top() != '[') {
						check = false;
						break;
					}
					else {
						s.pop();
					}
				}
			}

			if (!s.empty()) {
				check = false;
			}

			if (check) {
				cout << "yes" << endl;
			}
			else {
				cout << "no" << endl;
			}

		}
	}
	
	return 0;
}
