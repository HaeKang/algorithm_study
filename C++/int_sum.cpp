#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
input = 15

output
7 + 8 = 15
4 + 5 + 6 = 15
1 + 2 + 3 + 4 + 5 = 15
3
*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, cnt = 0;

	cin >> n;

	int tmp = n;

	n--;
	int a = 1;	// 몇자리로 덧셈
	while (n > 0) {
		a++;
		n = n - a;

		if (n % a == 0) {
			for (int i = 1; i < a; i++) {
				cout << n / a + i << "+ ";
			}
			cout << n / a + a << " = " << tmp << endl;
			cnt++;
		}


	}
	
	return 0;
}
