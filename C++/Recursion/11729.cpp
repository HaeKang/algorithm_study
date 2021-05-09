#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<pair<int, int>> v;
int n;
int cnt; 

void hanoi(int start, int sub, int end, int n) {
	if (n == 1) {
		v.push_back(make_pair(start, end));
		cnt++;
	}
	else {
		hanoi(start, end, sub, n - 1);
		v.push_back(make_pair(start, end));
		cnt++;
		hanoi(sub, start, end, n - 1);
	}
}

int main() {
	scanf("%d", &n);

	hanoi(1, 2, 3, n);

	printf("%d\n", cnt);
	for (int i = 0; i < v.size(); i++) {
		printf("%d %d\n", v[i].first, v[i].second);
	}
	return 0;
}
