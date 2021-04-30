#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string str1, str2;
int ans = 0;
int arr1[26];
int arr2[26];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> str1;
	cin >> str2;

	for (int i = 0; i < str1.size(); i++) {
		arr1[str1[i] - 'a']++;
	}
	
	for (int j = 0; j < str2.size(); j++) {
		arr2[str2[j] - 'a']++;
	}

	for (int k = 0; k < 26; k++) {
		if (arr1[k] != arr2[k]) {
			ans += abs(arr1[k] - arr2[k]);
		}
	}

	cout << ans << endl;
	return 0;
}
