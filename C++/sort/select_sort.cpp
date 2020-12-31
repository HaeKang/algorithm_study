#include <iostream>

void selection_sort(int list[], int n){
  for(int i=0; i<n; i++){
    int idx = i;
    
    for(int j=i+1; j<n; j++){
      if(list[j] < list[idx]){
        idx = j;
      }
    }
    
    if(idx != i){
      int tmp = list[i];
      list[i] = list[idx];
      list[idx] = tmp;
    }
    
  }
}

int main(){
  ios::sync_with_stdio(false);
	cin.tie(NULL);
  
  int n;
  cin >> n;
  
  int list[101];
  
  for(int i=0; i<n; i++){
    cin >> list[i];
  }
  
  selection_sort(list, n);
 
}
