#include <string>
#include <vector>
#include <algorithm>

#include <iostream>
using namespace std;

int solution(vector<int> a)
{
    int answer = 0;
    vector <int> cnt(a.size());
    
    for(int i =0;i<a.size();i++){
        cnt[a[i]]++;
    }
    
    for(int i=0;i<cnt.size();i++){
       
        if(cnt[i]<=answer){
            continue;
        }
        
        int result=0;
        
        for(int j=0; j<a.size()-1; j++){
            if((a[j] ==i or a[j+1] ==i)and a[j]!=a[j+1]){//
                result++;
                j++;
            }
            
            
        }
        
        answer=max(answer,result);
    }
    
    return answer*2;
}
