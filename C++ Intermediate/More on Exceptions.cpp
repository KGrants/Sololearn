#include <iostream>
using namespace std;

int main() {
    string menu[] = {"fruits", "chicken", "fish", "cake"};
    try {
        int x;
        cin >> x;
        if (x<0 or x>3)
            throw 404;
        else
            cout << menu[x] << endl;
        
    }
    catch(int a) {
        if (a==404){
            cout << "404 - not found" << endl;
        }
        
    
    }
}
