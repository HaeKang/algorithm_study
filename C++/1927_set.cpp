#include <iostream>
#include <stdio.h>
#include <cstring>
#include <set>
#include <algorithm>

#define MAX 100001

using namespace std;

int n;
multiset<int> s;
multiset<int>::iterator it;

int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x);
		if (x == 0) {
			if (!s.empty()) {
				it = s.begin();
				printf("%d\n", *it);
				s.erase(it);
			}
			else {
				printf("0\n");
			}
		}
		else {
			s.insert(x);
		}
	}
	return 0;
}
