#include <iostream>

using namespace std;

struct Node {
	int left;
	int right;
};

Node a[50];

void preorder(int x) {
	if (x == -1) return;
	cout << (char)(x + 'A');	//root
	preorder(a[x].left);		// 왼
	preorder(a[x].right);		// 오
}

void inorder(int x) {
	if (x == -1) return;
	inorder(a[x].left);		//왼
	cout << (char)(x + 'A');	//root
	inorder(a[x].right);		// 오
}

void postorder(int x) {
	if (x == -1) return;
	postorder(a[x].left);		// 왼
	postorder(a[x].right);		// 오
	cout << (char)(x + 'A');	// root
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {

		char x, y, z;
		cin >> x >> y >> z;
		x = x - 'A';

		if (y == '.') {
			a[x].left = -1;
		}
		else {
			a[x].left = y - 'A';
		}
		if (z == '.') {
			a[x].right = -1;
		}
		else {
			a[x].right = z - 'A';
		}
	}

	preorder(0);
	cout << '\n';

	inorder(0);
	cout << '\n';

	postorder(0);
	cout << '\n';

	return 0;
}