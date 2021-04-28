#include <iostream>
#include <string>
using namespace std;

int a, b, c;
int arr[10];

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> a;
	cin >> b;
	cin >> c;

	int abc = a * b*c;
	string abc_str = to_string(abc);

	for (int i = 0; i < abc_str.size(); i++) {
		int idx = abc_str[i] - '0';
		arr[idx]++;
	}


	for (int i = 0; i < 10; i++) {
		cout << arr[i] << endl;
	}
	
	return 0;
}
