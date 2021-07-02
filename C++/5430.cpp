#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <string>
using namespace std;

int t;



void solve(string fun, vector<int> arr) {

}

int main() {
	ios_base::sync_with_stdio(true);
	cin.tie(nullptr);

	cin >> t;

	while (t--) {
		string str1;	// function
		cin >> str1;

		int n;
		cin >> n;

		string str2;	// array
		cin >> str2;

		deque<int> d;
		string num_str;
 		for (int i = 0; i < str2.size(); i++) {
			if (str2[i] == '[') {
				continue;
			}
			if (str2[i] == ',' || str2[i] == ']') {
				if (num_str.empty()) {
					continue;
				}
				d.push_back(stoi(num_str));
				num_str.clear();
			}
			else {
				num_str += str2[i];
			}

		}

		bool state = true;
		bool reverse = false;
		
		for (int i = 0; i < str1.size(); i++) {

			if (str1[i] == 'R') {
				reverse = !reverse;
			}

			if (str1[i] == 'D') {
				if (d.empty()) {
					cout << "error" << '\n';
					state = false;
					break;
				}

				if (reverse) {
					d.pop_back();
				}
				else {
					d.pop_front();
				}
			}

		}

		

		if (state) {
			cout << "[";
			
			if (d.size() > 0) {
				if (reverse) {
					while (d.size() > 1) {
						cout << d.back() << ",";
						d.pop_back();
					}
					cout << d.back();
				}
				else {
					while (d.size() > 1) {
						cout << d.front() << ",";
						d.pop_front();
					}
					cout << d.front();
				}

			}

			cout << "]\n";
		}

	}

	return 0;
}
