#include <iostream>
#include <cstdio>
#include <set>
#include <string>
#include <algorithm>

#define MAX 500001

using namespace std;

int n, m;
set<string> nList;
set<string> ansList;
set<string>::iterator it;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		string n;
		cin >> n;
		nList.insert(n);
	}
	
	for (int i = 0; i < m; i++) {
		string n;
		cin >> n;

		it = nList.find(n);
		if (it != nList.end()) {
			ansList.insert(n);
		}
		
	}

	cout << ansList.size() << endl;
	for (it = ansList.begin(); it != ansList.end(); it++) {
		cout << *it<< endl;
	}
	
	return 0;
}
