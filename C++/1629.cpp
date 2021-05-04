#include <iostream>
#include <string>
#include <queue>
#include <cstring>

using namespace std;

long long a, b, c;

long long fun(long long a, long long b, long long c) {
	if (b == 1) {
		return a % c;
	}

	long long num = fun(a, b / 2, c);
	num = num * num % c;

	if (b % 2 != 0) {
		return num * a % c;
	}
	else {
		return num;
	}

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> a >> b >> c;

	cout << fun(a, b, c) << endl;

	return 0;
}
