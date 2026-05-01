/*
lengli_QAQ
Hope there are no bugs!!!
*/
#include <bits/stdc++.h>
#define fastio std::ios::sync_with_stdio(0); std::cin.tie(0); std::cout.tie(0)
#define all(x) x.begin(),x.end()
#define pb push_back
#define i64 long long

void solve(){
    std::string a,b;
    std::cin>>a>>b;
    int n=a.size();

    std::string A="&#",B="&#";
    for(auto x:a) A+=x,A+='#';A+='%';
    for(auto x:b) B+=x,B+='#';B+='%';


    int len=A.size();
    std::vector<int> P(len),pre(len),suf(len);

    int mid=0,r=0;

    auto check=[&](int l,int r){
        return A[l]==A[r] and B[l]==B[r];
    };
    for(int i=1;i<len-1;i++){
        if(r>i) P[i]=std::min(r-i,P[2*mid-i]);
        else P[i]=1;
        while(check(i-P[i],i+P[i])) P[i]++;
        if(i+P[i]>r){
            mid=i;
            r=i+P[i];
        }
        pre[i-P[i]+1]++;
        pre[i+1]--;
        suf[i]++;
        suf[i+P[i]]--;
    }

    for(int i=1;i<len;i++) pre[i]+=pre[i-1],suf[i]+=suf[i-1];

    i64 res=0;

    for(int i=2,j=n*2;i<=n*2;i+=2,j-=2){
        if(A[i]!=B[j] or B[i]!=A[j]) break;
        res+=suf[j-2]+pre[i+2]+1;
    }

    std::cout<<res<<"\n";

}

signed main(){
    fastio;
    
    int T;
    std::cin>>T;
    while(T--) solve();
    
    return 0;
}
