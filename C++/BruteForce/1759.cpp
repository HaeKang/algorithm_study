#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

bool check(string &pw) {
	int ja = 0;	// 자음
	int mo = 0;	// 모음

	for (char x : pw) {
		if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
			mo += 1;
		}
		else {
			ja += 1;
		}
	}
	return ja >= 2 && mo >= 1;
}

void go(int n, vector<char> &alpha, string pw, int i) {
	if (pw.length() == n) {
		if (check(pw)) {
			cout << pw << '\n';
		}
		return;
	}

	if (i == alpha.size()) {
		return;
	}

	go(n, alpha, pw + alpha[i], i + 1);	// 사용
	go(n, alpha, pw, i + 1);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	cin >> n >> m;
	vector<char> a(m);
	for (int i = 0; i<m; i++) {
		cin >> a[i];
	}

	sort(a.begin(), a.end());

	go(n, a, "", 0);

	return 0;
}
