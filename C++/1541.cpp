#include <iostream>
#include <string>
using namespace std;

string input;
string tmp;
int ans = 0;
bool par = false;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> input;

	for (int i = 0; i <= input.size(); i++) {
		char tmp_char = input[i];
		if (tmp_char == '-' || tmp_char == '+' || tmp_char == '\0') {		
			if (par) {
				ans -= stoi(tmp);
			}
			else {
				ans += stoi(tmp);
			}

			if (tmp_char == '-') {
				par = true;	// 괄호 open
			}

			tmp = "";
		}
		else {
			tmp += tmp_char;
		}
	}

	cout << ans;
	return 0;

}
