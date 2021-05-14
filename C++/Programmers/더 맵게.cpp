#include <string>
#include <vector>
#include <queue>

using namespace std;

priority_queue<int,vector<int>,greater<int>> q;

int solution(vector<int> scoville, int k) {
    int answer = 0;
    
    for(int i=0; i<scoville.size(); i++){
        q.push(scoville[i]);
    }
    
    while(q.top()<k && q.size() > 1){
        int score1 = q.top();
        q.pop();

        int score2 = q.top();
        q.pop();
        
        int mix_score = score1 + (score2 * 2);
        q.push(mix_score);
        answer++;
    }
    
    if(q.top() < k){
        answer = -1;
    }
    return answer;
}
