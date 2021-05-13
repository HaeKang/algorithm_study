#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days;
    
    for(int i=0; i<progresses.size(); i++){
        int state = 100 - progresses[i];
        int speed = speeds[i];
        
        if(state % speed > 0){
            days.push_back(state/speed + 1);
        } else {
            days.push_back(state/speed);
        }
    }
    
    queue<int> q;
    q.push(days[0]);

    
    for(int i=1; i<days.size(); i++){
        if(q.front() >= days[i]){
            q.push(days[i]);
        } else {
            answer.push_back(q.size());
            while(!q.empty()){
                q.pop();
            }
            q.push(days[i]);
        }
    }
    
    if(!q.empty()){
        answer.push_back(q.size());
    }
    return answer;
}
