#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(vector<int> numbers, int sum, int cnt, int target){
    if(cnt == numbers.size()){
        if(sum == target){
            answer++;
            return;
        } else {
            return;
        }
    }
    
    dfs(numbers, sum + numbers[cnt], cnt+1, target);
    dfs(numbers, sum - numbers[cnt], cnt+1, target);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, 0,0,target);
    return answer;
}
