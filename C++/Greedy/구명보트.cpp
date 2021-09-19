#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    int left = 0;
    int right = people.size() - 1;
    
    sort(people.begin(), people.end());
    
        
    while (true){
        if (left > right){
            break;
        }
        
            
        if(people[left] + people[right] <= limit){
            left += 1;
            right -= 1;
        } else{
            right -= 1;
        }
        
        answer += 1;
        
        if (left == right){
            answer  += 1;
            break;
        }
    }
    
    
    
    return answer;
}
