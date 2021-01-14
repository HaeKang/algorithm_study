#include <iostream>
#include <cstdio>
#include <string>
#include <map>

#define MAX 100001

using namespace std;

int n, m;

map<string, int> d;
string d2[MAX];

int main() {

	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; i++) {
		char tmp[21];
		scanf("%s", tmp);
		string name = tmp;

		d.insert(pair<string, int>(name, i));
		d2[i] = name;
	}

	for (int i = 0; i < m; i++) {
		char tmp[21];
		scanf("%s", tmp);
		string input = tmp;

		if (atoi(input.c_str()) != 0) {	// 숫자일경우
			int input_num = stoi(input);
			printf("%s\n", d2[input_num-1].c_str());
		}
		else {
			printf("%d\n", d[input] +1);
		}

	}


	return 0;

}
