#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool check(string a, string b){
    if(a+b > b+a){
        return true;    // a > b
    } else {
        return false;   // b > a
    }
}

string solution(vector<int> numbers) {
    string answer = "";
    
    vector<string> v;
    for(int i=0; i<numbers.size(); i++){
        v.push_back(to_string(numbers[i]));
    }
    
    sort(v.begin(), v.end(), check);
    
    if(v[0] == "0"){
        return "0";
    }
    
    for(int i=0; i<v.size(); i++){
        answer += v[i];
    }
    return answer;
}
