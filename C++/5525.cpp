#include <iostream>
#include <string>
using namespace std;

int n, m, cnt, ans;
string s;

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> n;	// OI의 개수
	cin >> m;
	cin >> s;


	for (int i = 0; i < m; i++) {
		if (s[i] == 'O') {
			continue;
		}

		while (s[i + 1] == 'O' && s[i + 2] == 'I') {
			cnt++;
			i += 2;
			if (cnt == n) {
				ans++;
				cnt--;
			}
		}
		cnt = 0;

	}

	cout << ans << '\n';
	return 0;
}
