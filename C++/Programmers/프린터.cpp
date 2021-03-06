#include <string>
#include <vector>
#include <queue>

using namespace std;

queue<int> wait;
queue<int> prior;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    for(int i=0; i<priorities.size(); i++){
        wait.push(i);   
        prior.push(priorities[i]);
    }
    
    while(!wait.empty()){
        int num = wait.front();
        int num_p = prior.front();
        wait.pop();
        prior.pop();
        
        bool check = false;
        queue<int> p_copy;
        p_copy = prior;
        while(!p_copy.empty()){
            if(num_p < p_copy.front()){
                check = true;
                break;
            }
            p_copy.pop();
        }
        
        if(check){
            wait.push(num);
            prior.push(num_p);
        } else {
            answer++;
            if(location == num){
                return answer;
            }
        }
    }
    
    return answer;
}


// 우선순위 큐 사용
#include <string>
#include <vector>
#include <queue>

using namespace std;

queue<pair<int,int>> wait;
priority_queue<int> prior;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    for(int i=0; i<priorities.size(); i++){
        wait.push(make_pair(i, priorities[i]));   
        prior.push(priorities[i]);
    }
    
    while(!wait.empty()){
        int num = wait.front().first;
        int num_p = wait.front().second;
        
        int top_p = prior.top();
    
        wait.pop();
        
        if(num_p < top_p){
            wait.push(make_pair(num, num_p));
        } else {
            answer++;
            prior.pop();
            if(location == num){
                return answer;
            }
        }
    }
    
    return answer;
}
