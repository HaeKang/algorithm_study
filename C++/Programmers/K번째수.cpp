#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int idx=0; idx<commands.size(); idx++){
        int i = commands[idx][0];
        int j = commands[idx][1];
        int k = commands[idx][2];
        
        vector<int> arr;
        for(int idx2 = i-1; idx2 < j; idx2++){
            arr.push_back(array[idx2]);
        }
        
        sort(arr.begin(), arr.end());
        answer.push_back(arr[k-1]);
    }
       
    return answer;
}
