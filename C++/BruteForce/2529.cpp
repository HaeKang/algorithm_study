#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int n;
char a[20];
vector<string> ans;
bool check[10];

bool ok(char x, char y, char op) {
	if (op == '<') {
		if (x > y) return false;
	}
	if (op == '>') {
		if (x < y) return false;
	}
	return true;
}

void go(int index, string num) {
	if (index == n + 1) {
		ans.push_back(num);
		return;
	}

	for (int i = 0; i <= 9; i++) {
		if (check[i]) {
			continue;
		}
		if (index == 0 || ok(num[index - 1], i + '0', a[index - 1])) {
			check[i] = true;
			go(index + 1, num + to_string(i));
			check[i] = false;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> n;
	for (int i = 0; i<n; i++) {
		cin >> a[i];
	}
	go(0, "");
	auto p = minmax_element(ans.begin(), ans.end());
	cout << *p.second << '\n';
	cout << *p.first << '\n';


	return 0;
}
