#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

#define MAX 500001

using namespace std;

int n, m;
vector<string> nList;
vector<string> ansList;
vector<string>::iterator it;

void binary(int lp, int rp, string name) {
	while (lp <= rp) {
		int mid = (lp + rp) / 2;

		if (!nList[mid].compare(name)) {
			ansList.push_back(name);
			return;
		}
		else if (nList[mid] < name) {
			lp = mid + 1;
		}
		else {
			rp = mid - 1;
		}
	}
	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		string n;
		cin >> n;
		nList.push_back(n);
	}
	
	sort(nList.begin(), nList.end());
	
	for (int i = 0; i < m; i++) {
		string n;
		cin >> n;

		binary(0, nList.size() - 1, n);
	}

	sort(ansList.begin(), ansList.end());
	cout << ansList.size() << endl;
	for (int i = 0; i < ansList.size(); i++) {
		cout << ansList[i] << endl;
	}
	
	return 0;
}
