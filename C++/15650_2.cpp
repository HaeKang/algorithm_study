#include <iostream>
using namespace std;

// ���ù������

int a[10];

// index��� ���� ����� �����Ұ���������, selected = ���ݱ��� ������ ���� ����
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
	
	// ���̻� �����Ұ� X
	if (index > n) {
		return;
	}

	// �����ϴ°��
	a[selected] = index;
	go(index + 1, selected + 1, n, m);

	// ����x
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
