#include <iostream>
using namespace std;

int main() {
    int evenSum,oddSum=0;
    int N;
    cout<<"Enter Number";
    cin>>N;
    while(N!=0)
    {
        int rem=N%10;
        if(rem%2==0)
        {
            evenSum+=evenSum;
        }
        else
        {
            oddSum+=oddSum;
        }
        N=N/10;
        
    }
    cout<<evenSum<<" "<<oddSum;

    return 0;
}