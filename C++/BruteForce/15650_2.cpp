#include <iostream>
using namespace std;

// 선택방법으로

int a[10];

// index라는 수를 결과에 포함할건지말건지, selected = 지금까지 선택한 수의 개수
void go(int index, int selected, int n, int m) {
	if (selected == m) {
		for (int i = 0; i < m; i++) {
			cout << a[i];
			if (i != m - 1) {
				cout << ' ';
			}
		}
		cout << '\n';
		return;
	}
	
	// 더이상 선택할거 X
	if (index > n) {
		return;
	}

	// 선택하는경우
	a[selected] = index;
	go(index + 1, selected + 1, n, m);

	// 선택x
	a[selected] = 0;
	go(index + 1, selected, n, m);


}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	cin >> n >> m;
	go(1,0 ,n, m);
	return 0;

}
