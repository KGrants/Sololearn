#include <iostream>
using namespace std;

class Number
{
    private:
        int num;
    public:
        Number(int n) {
            num = n;
        }
        //complete the method
        int square() const {
           return num*num;
        };
};

int main() {
    int x;
    cin >> x;
    const Number myNum(x);
    cout << myNum.square();
}