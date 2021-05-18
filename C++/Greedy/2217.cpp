#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> v, v2;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		int w;
		cin >> w;
		v.push_back(w);
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < v.size(); i++) {
		int w2 = v[i];
		v2.push_back(w2 * (v.size() - i));
	}
	cout << *max_element(v2.begin(), v2.end()) << '\n';

	return 0;
}
