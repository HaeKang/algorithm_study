#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int s1[5] = {1,2,3,4,5};
int s2[8] = {2,1,2,3,2,4,2,5};
int s3[10] = {3,3,1,1,2,2,4,4,5,5};

vector<int> score(3,0);

vector<int> solution(vector<int> answers) {
    vector<int> answer;


    for(int i=0; i<answers.size(); i++){
        if(s1[i%5] == answers[i]){
            score[0]++;
        }
        if(s2[i%8] == answers[i]){
            score[1]++;
        }
        if(s3[i%10] == answers[i]){
            score[2]++;
        }
    }
    
    
    int max_score = *max_element(score.begin(), score.end());
    
    for(int i=0; i<3; i++){
        if(max_score == score[i]){
            answer.push_back(i+1);
        }
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}
