#include <iostream>
#include <string>
using namespace std;

int arr[26];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	cin >> s;

	for (int k = 0; k < s.size(); k++) {
		arr[s[k] - 97]++;
	}

	for (int i = 0; i < 26; i++) {
		cout << arr[i] << ' ';
	}

	return 0;
}
