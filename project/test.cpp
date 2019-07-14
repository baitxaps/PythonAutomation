#include<iostream>
#include<string>
using namespace std;

int main() {    
    string s = "hello.";    
    for(int i = 0; i < s.length(); ++i) {        
        cout << s[i] << endl;    
    }   
    system("pause");    
    return 0;
}
