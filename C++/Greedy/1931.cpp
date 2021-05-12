#include <cstdio>
#include <algorithm>
#include <vector>

#define MAX 100001

using namespace std;

int n;
int next_time = 0, ans = 0;
vector<pair<int, int>> time;

int main() {

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		int start, end;
		scanf("%d %d", &start, &end);
		time.push_back(make_pair(end, start));
	}

	sort(time.begin(), time.end());

	for (int j = 0; j < time.size(); j++) {
		int meet_start = time[j].second;
		int meet_end = time[j].first;
		if (next_time <= meet_start) {
			next_time = meet_end;
			ans++;
		}
	}

	printf("%d", ans);
	
	return 0;
}
