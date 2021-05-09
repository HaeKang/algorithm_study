#include <iostream>
#include <string>
#include <stack>
#define MAX 1000001

using namespace std;

int n;
int a[MAX];
int freq[MAX];
int ngf[MAX];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
		freq[a[i]]++;
	}

	stack<int> s;
	s.push(0);	// index num

	for (int i = 1; i < n; i++) {

		while (!s.empty() && freq[a[i]] > freq[a[s.top()]] ) {
			ngf[s.top()] = a[i];
			s.pop();
		}

		s.push(i);
	}


	// 오등큰수 x 경우
	while (!s.empty()) {
		ngf[s.top()] = -1;
		s.pop();
	}


	for (int i = 0; i < n; i++) {
		cout << ngf[i] << ' ';
	}

	return 0;
}
