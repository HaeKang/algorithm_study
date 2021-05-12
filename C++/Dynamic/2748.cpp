#include <cstdio>

using namespace std;

int n;
long long fibo[92];

int main() {
	scanf("%d", &n);
	fibo[0] = 0;
	fibo[1] = 1;

	for (int i = 2; i <= n; i++) {
		fibo[i] = fibo[i - 2] + fibo[i - 1];
	}
	
	printf("%lld\n", fibo[n]);
	return 0;
}
