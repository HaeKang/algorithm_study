#include <iostream>
#include <string>
#include <stack>
using namespace std;

string str;
int ans;
int tmp = 1;
bool check;

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> str;

	stack<char> s;
	check = true;

	for (int i = 0; i < str.size(); i++) {

		if (str[i] == '(' || str[i] == '[') {
			if (str[i] == '(') {
				tmp *= 2;
			}
			else {
				tmp *= 3;
			}
			s.push(str[i]);
		}

		else if (str[i] == ')') {
			if (s.empty() || s.top() != '(') {
				check = false;
				break;
			}
			else {
				if (str[i - 1] == '(') {
					ans += tmp;
				}
				s.pop();
				tmp /= 2;
			}
		}

		else if (str[i] == ']') {
			if (s.empty() || s.top() != '[') {
				check = false;
				break;
			}
			else {
				if (str[i - 1] == '[') {
					ans += tmp;
				}
				s.pop();
				tmp /= 3;
			}
		}

	}

	if (check && s.empty()) {
		cout << ans << '\n';
	}
	else {
		cout << "0\n";
	}

	return 0;
}
