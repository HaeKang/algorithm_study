#include <iostream>
#include <map>
#include <string>
using namespace std;

int t, n, ans;
string s1, s2;
map<string, int> m;
map<string, int>::iterator it;

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> t;

	while (t--) {
		n = 0;
		ans = 1;
		m.clear();

		cin >> n;

		for (int i = 0; i < n; i++) {
			s1.clear();
			s2.clear();
			cin >> s1 >> s2;

			if (m.find(s2) != m.end()) {
				m[s2]++;
			}
			else {
				m.insert({s2,1});
			}
			
		}


		for (it = m.begin(); it != m.end(); it++) {
			int cnt = it->second;
			ans *= (cnt + 1);
		}

		cout << ans - 1 << '\n';
	}

	return 0;
}
